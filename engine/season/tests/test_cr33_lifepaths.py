"""v10 CR-33: the 34 lifepaths as creation templates -- capability keys HELD, the lifepath never a field.

FALSIFIER (the plan's): a cast row whose lifepath maps to `inquiry` builds with `capability == {"inquiry":
pool_default}`, rolls the same pool on `research` as a row with no lifepath, and `train` on `inquiry` executes for
it and is refused for the other; a template naming a key outside `descriptors.CAPABILITIES` is refused at import;
`repr(Person)` contains no lifepath id. PLANTED FAILURE: the expansion skipped reddens the `train` assertion (run
in-test below, `test_the_planted_failure_...`). CONTROL: the one-season hash with the expansion skipped differs from the
shipped one (the shipped state's movers are NPC-004's and NPC-088's `inquiry`); the shipped hash is `_realm_goldens.py`'s.

Built on `build_realm` with a PLANTED `lifepath:` on a row that authors none (NPC-030), so the falsifier does not
read the registry's own authoring; the registry's authored set is pinned separately.
"""
import dataclasses

import pytest

from engine.dice_engine.sigma_leverage import pool_of
from engine.season.data import cast
from engine.season.data import rosters as R
from engine.substrate.descriptors import CAPABILITIES
from engine.season.decision import assemble
from engine.season.decision.options import opening_set
from engine.season.gaps import Unspecified
from engine.season.boot.realm import build_realm
from engine.season.loop.driver import SeasonDriver, mint_token
from engine.season.seam.wrappers import pool, sigma
from engine.season.state.carriers import Act, Person, Question
from engine.season.state.gate import WriteClass
from ._flat_fold import flat_fold
from .test_in10_record_operands import _resolve

pytestmark = pytest.mark.flat_fold

#: The four Niflhel ids the archived file STRIKES (it prints no row for them): never members.
STRUCK = ("3-NI1", "3-NI2", "3-NI3", "3-NI4")

PLANTED, OTHER = "NPC-030", "NPC-031"                   # two rows that author no lifepath and (BA1.99: re-picked from NPC-087, NPC-084, which BA1.01 authors `argue: 3` on) no `capabilities:`
P_ID, Q_ID = "p_npc_030", "p_npc_031"
LIFEPATH_TO_INQUIRY = "3-CH5"                           # Church Investigator: `holds: [inquiry]`

#: `{case id: lifepath}` -- the whole authored set, pinned so a key added without its row's own text reddens here.
AUTHORED = {"NPC-002": "3-VA1",     # notes: "Vaynard's intelligence operative" (Varfell)
            "NPC-004": "3-CH5",     # role: "Field Inquisitor", goal "Investigate heresy" (added by the verify pass)
            "NPC-005": "3-LO3",     # role: "TS Riskbreaker (Covert)"
            "NPC-080": "3-LO3",     # role: "Riskbreaker (doctrine-following ...)"
            "NPC-088": "3-CF4"}     # role: "Copyist (hand-copies suppressed Einhir cultural texts)"


# ======================================================================================
# THE ROSTER AND THE LOADER: closed both ways
# ======================================================================================

def test_the_roster_is_the_34_and_the_struck_niflhel_ids_are_not_members():
    assert len(R.LIFEPATHS) == 34 and not set(STRUCK) & set(R.LIFEPATHS)
    assert set(R.LIFEPATH_TEMPLATES) == set(R.LIFEPATHS)


def test_every_template_names_only_defined_skills():
    names = set(CAPABILITIES)
    held = [k for keys in R.LIFEPATH_TEMPLATES.values() for k in keys]
    assert held and set(held) <= names
    assert any(not keys for keys in R.LIFEPATH_TEMPLATES.values()), "no row maps to none: the cut invented one"


def _cells():
    return R.table("lifepath_templates")


@pytest.mark.parametrize("mutate", [
    lambda c: c["3-CR4"].update(holds=["no_such_vocation"]),        # a key outside `descriptors.CAPABILITIES` (B04.04: a skill no verb names is still a defined skill)
    lambda c: c.update({"3-NI1": {"holds": [], "ground": "x"}}),    # an id outside the 34 (a struck one)
    lambda c: c.pop("3-CF6"),                                       # a lifepath with no row
    lambda c: c["3-CR1"].update(holds=["argue", "argue"]),          # a key held twice
    lambda c: c["3-CR2"].update(ground=""),                         # a row with no ground
    lambda c: c["3-CR3"].update(holds="argue"),                     # `holds:` not a list
])
def test_a_template_outside_the_closed_set_is_refused_at_import(mutate):
    cells = {k: dict(v) for k, v in _cells().items()}
    mutate(cells)
    with pytest.raises(Unspecified):
        R._load_lifepaths(cells, R.LIFEPATHS, frozenset(CAPABILITIES))


def test_the_shipped_cells_pass_the_same_loader():
    assert R._load_lifepaths(_cells(), R.LIFEPATHS, frozenset(CAPABILITIES)) == (R.LIFEPATH_TEMPLATES, R.LIFEPATH_RANKS)


# ======================================================================================
# THE CAST KEY
# ======================================================================================

def test_the_expansion_holds_each_key_at_pool_default_and_silence_is_no_key():
    assert cast.capability_of({"id": "X", "lifepath": LIFEPATH_TO_INQUIRY}, 2) == {"inquiry": 2}
    assert cast.capability_of({"id": "X", "lifepath": LIFEPATH_TO_INQUIRY}, 5) == {"inquiry": 5}
    assert cast.capability_of({"id": "X", "lifepath": "3-CR2"}, 2) == {}, "a lifepath that maps to none grants none"
    assert cast.capability_of({}, 2) == {} and cast.capability_of({"id": "X"}, 2) == {}
    assert cast.capability_of({"id": "X", "lifepath": None}, 2) == {}


@pytest.mark.parametrize("raw", ["3-NI1", "3-cr1", "vocation", "", 3, ["3-CR1"], True])
def test_a_cast_row_naming_no_template_is_refused(raw):
    with pytest.raises(Unspecified):
        cast.capability_of({"id": "X", "lifepath": raw}, 2)


def test_the_registry_authors_only_rows_whose_own_text_states_a_lifepath():
    authored = {cid: r["lifepath"] for cid, r in cast.load().items() if r.get("lifepath") is not None}
    assert authored == AUTHORED
    for cid, r in cast.load().items():
        cast.capability_of(r, 2)                                   # every authored key validates


# ======================================================================================
# THE FALSIFIER: a planted row, built through `build_realm`
# ======================================================================================

def _planted_cache():
    rows = {cid: dict(r) for cid, r in cast.load().items()}
    rows[PLANTED]["lifepath"] = LIFEPATH_TO_INQUIRY
    return rows


def _world(monkeypatch, planted=True):
    monkeypatch.setattr(cast, "_CACHE", _planted_cache() if planted else cast._CACHE)
    w = flat_fold(build_realm(0))      # module-scoped callers build before the function-scoped mark applies
    d = SeasonDriver(w)
    d.matter(mint_token(w, WriteClass.MATTER), [])
    return w, d


def _train(w, d, pid, key="inquiry", act_id="tr"):
    return [e.kind for e in _resolve(w, d, Act(id=f"{act_id}_{pid}", actor=pid, verb="train",
                                                payload={"subject": pid, "kind": key}))]


@pytest.fixture(scope="module")
def planted_world():
    with pytest.MonkeyPatch.context() as m:
        yield _world(m)


def test_a_planted_lifepath_builds_the_key_held_at_pool_default_and_rolls_the_same_pool(planted_world):
    w, _d = planted_world
    default = w.fixtures.get("pool_default")
    p, q = w.persons[P_ID], w.persons[Q_ID]
    assert p.capability == {"inquiry": default} and q.capability == {}
    # B05.99 rewrite (B05.25: the pool is `pool_of(governing score + rank, addends, pool_add, pool_floor)`; was the larger of the
    # attribute and the key): the key held at `pool_default` ADDS its rank over the person's governing score; the holder of
    # nothing reads his governing score alone.
    att = lambda x: pool.governing_attribute(x, "research")
    assert att(p) is not None and att(q) is not None, "the drawn sheets seat the verb's governing attributes on both"
    fx = w.fixtures
    rolled = lambda x, rank: pool_of(pool.governing_score(w, x, "research") + rank, pool.addends_of(w, x, "research"),
                                     fx.get("pool_add"), fx.get("pool_floor"))
    assert pool.rank(p, "research") == default and pool.rank(q, "research") == 0
    assert sigma.faculty(w, p, "research") == rolled(p, default)
    assert sigma.faculty(w, q, "research") == rolled(q, 0)
    # BA1.99 re-point (BA1.01 authors `capabilities:` scores on 40 rows, which win over the lifepath expansion): the holders are exactly the
    # rows whose expansion or authored scores name a key, each at the expansion merged under the authored scores -- so the planted row holds
    # `inquiry` at `pool_default` and a lifepath row whose `capabilities:` names `inquiry` (NPC-004, NPC-088) holds the authored score.
    expected = {f"p_{cid.lower().replace('-', '_')}": {**cast.capability_of(r, default), **cast.capabilities_of(r)}
                for cid, r in _planted_cache().items()}
    expected = {pid: cap for pid, cap in expected.items() if cap}
    holders = {pid: x.capability for pid, x in w.persons.items() if x.capability}
    assert len(expected) >= 40 and holders == expected, holders
    assert holders[P_ID] == {"inquiry": default}
    assert holders["p_npc_004"]["inquiry"] == cast.capabilities_of(cast.row("NPC-004"))["inquiry"] != default


def test_train_on_inquiry_raises_the_holder_and_mints_the_other_a_first_rank(planted_world):
    """B05.09 (CORE Edit 9; B05.99 rewrite): `train` on a non-holder mints a first rank (was `train.refused`); the holder's key
    rises by one, and so does his pool (B05.25: every rank is a die over his governing score)."""
    w, d = planted_world
    default = w.fixtures.get("pool_default")
    before = sigma.faculty(w, w.persons[P_ID], "research")
    assert _train(w, d, Q_ID) == ["capability.raised"] and w.persons[Q_ID].capability == {"inquiry": 1}
    assert _train(w, d, P_ID) == ["capability.raised"]
    assert w.persons[P_ID].capability == {"inquiry": default + 1}
    assert sigma.faculty(w, w.persons[P_ID], "research") == before + 1, "the raised key is not in the pool"


def test_the_lifepath_id_is_stored_nowhere_on_a_person(planted_world):
    w, _d = planted_world
    p = w.persons[P_ID]
    assert LIFEPATH_TO_INQUIRY not in repr(p)
    assert not [f.name for f in dataclasses.fields(Person) if "lifepath" in f.name or "vocation" in f.name]
    assert not any(LIFEPATH_TO_INQUIRY in repr(x) for x in w.persons.values())


# ======================================================================================
# PLANTED FAILURE AND CONTROL
# ======================================================================================
