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
from engine.season.data.verbs import EVENT_KINDS, VERB_TABLE, _check_strife_kinds
from engine.season.gaps import Unspecified
from engine.season.harness import strife_data as data
from engine.season.queries import world_q as W

LISTS = tuple(sorted(R.STRIFE_KINDS))      # the four lists, read off the loader and not spelled again
DECIDED = tuple(n for n in LISTS if n != "concludes")   # opens, joins, never: a decision per kind


def _planted(**add):
    """A copy of the shipped lists as sets, with each `add` (list name -> kinds) added to its list."""
    return {n: set(R.STRIFE_KINDS[n]) | set(add.get(n, ())) for n in LISTS}


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


# The control for the three plants below is the import itself: it ran `_check_strife_kinds` on the shipped lists.
def test_import_check_refuses_a_kind_outside_event_kinds():
    with pytest.raises(Unspecified, match="nonesuch.kind"):
        _check_strife_kinds(_planted(never={"nonesuch.kind"}), EVENT_KINDS)


def test_import_check_refuses_a_kind_in_two_lists():
    with pytest.raises(Unspecified, match="field.won"):                       # field.won is in `opens`
        _check_strife_kinds(_planted(never={"field.won"}), EVENT_KINDS)


def test_import_check_refuses_a_concludes_kind_outside_opens_and_joins():
    with pytest.raises(Unspecified, match="news.told"):                       # news.told is `never`
        _check_strife_kinds(_planted(concludes={"news.told"}), EVENT_KINDS)


def test_loader_refuses_a_malformed_block():
    base = {n: sorted(v) for n, v in _planted().items()}    # the loader reads lists
    with pytest.raises(Unspecified):
        R._load_strife_kinds({**base, "extra": ["field.won"]})                                  # a list nobody reads
    with pytest.raises(Unspecified):
        R._load_strife_kinds({k: v for k, v in base.items() if k != "never"})                   # a decision nobody made
    with pytest.raises(Unspecified):
        R._load_strife_kinds({**base, "never": []})                                             # empty is not absent-but-fine
    with pytest.raises(Unspecified):
        R._load_strife_kinds({**base, "opens": base["opens"] + [base["opens"][0]]})             # a kind twice in one list


def _homeless(registry, lists) -> dict:
    """`{kind: [the lists of opens/joins/never holding it]}` for every registry kind NOT in exactly one of them:
    the one predicate the test and its falsifier both read."""
    out = {}
    for k in sorted(registry):
        homes = [n for n in DECIDED if k in lists[n]]
        if len(homes) != 1:
            out[k] = homes
    return out


def test_every_registry_kind_is_in_exactly_one_of_opens_joins_never():
    registry = {k for r in data.MOVES for k in r["kinds"]}
    assert len(registry) >= 40     # the control: a registry that read empty would pass the check below
    assert _homeless(registry, R.STRIFE_KINDS) == {}


def test_a_registry_kind_in_none_of_the_three_lists_is_seen():
    # FALSIFIER of the test above: strike one registry kind from its list and the same predicate finds the hole.
    registry = {k for r in data.MOVES for k in r["kinds"]}
    struck = {n: set(R.STRIFE_KINDS[n]) - {"tenure.opened"} for n in LISTS}
    assert _homeless(registry, struck) == {"tenure.opened": []}


def test_concludes_equals_the_rule_derived_over_the_registry():
    lists = {n: R.STRIFE_KINDS[n] for n in LISTS}
    derived = derive_concludes(data.MOVES, lists)
    assert derived and derived == R.STRIFE_KINDS["concludes"], (
        f"only in the derivation: {sorted(derived - R.STRIFE_KINDS['concludes'])}; "
        f"only in rosters.yaml: {sorted(R.STRIFE_KINDS['concludes'] - derived)}")


def test_mutation_requisition_taken_in_concludes_passes_the_import_check_and_fails_the_derivation():
    mutated = _planted(concludes={"requisition.taken"})
    _check_strife_kinds(mutated, EVENT_KINDS)           # in `opens`, so the loader's check cannot see it
    derived = derive_concludes(data.MOVES, mutated)
    assert derived != mutated["concludes"]
    assert mutated["concludes"] - derived == {"requisition.taken"}     # VI never ends a case


def test_foreign_faction_ids_are_the_roster_names_as_propositions():
    assert R.FOREIGN_FACTION_IDS == {R.faction_prop_id(f) for f in R.FOREIGN_FACTIONS}


# The world reading's openers (`world_q.check_strife_openers`, run at import on the shipped tables): each refusal
# planted on the function, the shipped call as its control.
def test_the_shipped_openers_pass_their_check():
    W.check_strife_openers(R.STRIFE_KINDS["joins"], VERB_TABLE, R.RECORD_KIND_KEYS)


def test_an_opener_kind_outside_joins_is_refused():
    joins = R.STRIFE_KINDS["joins"] - {W.OPENING_MARCH_KIND}
    with pytest.raises(Unspecified, match=W.OPENING_MARCH_KIND):
        W.check_strife_openers(joins, VERB_TABLE, R.RECORD_KIND_KEYS)


@pytest.mark.parametrize("verb", [W.OPENING_MARCH_VERB, *sorted(W.OPENING_DEATH_VERBS)])
def test_an_opener_verb_outside_the_verb_table_is_refused(verb):
    table = {k: v for k, v in VERB_TABLE.items() if k != verb}
    with pytest.raises(Unspecified, match=f"'{verb}'"):
        W.check_strife_openers(R.STRIFE_KINDS["joins"], table, R.RECORD_KIND_KEYS)


def test_a_petition_record_without_its_matter_key_is_refused():
    keys = {**R.RECORD_KIND_KEYS,
            W.PETITION_RECORD_KIND: [k for k in R.RECORD_KIND_KEYS[W.PETITION_RECORD_KIND] if k != W.PETITION_MATTER_KEY]}
    with pytest.raises(Unspecified, match=W.PETITION_MATTER_KEY):
        W.check_strife_openers(R.STRIFE_KINDS["joins"], VERB_TABLE, keys)


def test_an_empty_restraint_derivation_is_refused():
    W.check_restraint_kinds(W.KNOWN_RESTRAINT_KINDS, W.KNOWN_RESTRAINT_ENDED_KINDS)     # the shipped call
    with pytest.raises(Unspecified, match="restraint arm"):
        W.check_restraint_kinds(frozenset(), W.KNOWN_RESTRAINT_ENDED_KINDS)
    with pytest.raises(Unspecified, match="restraint arm"):
        W.check_restraint_kinds(W.KNOWN_RESTRAINT_KINDS, frozenset())
