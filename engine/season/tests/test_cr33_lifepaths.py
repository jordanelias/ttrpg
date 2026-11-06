"""v10 CR-33: the 34 lifepaths as creation templates -- capability keys HELD, the lifepath never a field.

FALSIFIER (the plan's): a cast row whose lifepath maps to `inquiry` builds with `capability == {"inquiry":
pool_default}`, rolls the same pool on `research` as a row with no lifepath, and `train` on `inquiry` executes for
it and is refused for the other; a template naming a key outside `verb_capability`'s values is refused at import;
`repr(Person)` contains no lifepath id. PLANTED FAILURE: the expansion skipped reddens the `train` assertion (run
in-test below, `test_the_planted_failure_...`). CONTROL: the expansion skipped reproduces the pre-commit hash with
the registry's authored rows in place (the shipped state's movers are NPC-004's and NPC-088's `inquiry`).

Built on `build_realm` with a PLANTED `lifepath:` on a row that authors none (NPC-087), so the falsifier does not
read the registry's own authoring; the registry's authored set is pinned separately.
"""
import dataclasses

import pytest

from engine.season.data import cast
from engine.season.data import rosters as R
from engine.season.data import verbs as VERBS
from engine.season.decision import assemble
from engine.season.decision.options import opening_set
from engine.season.gaps import Unspecified
from engine.season.harness import populated as PO
from engine.season.loop.driver import SeasonDriver, mint_token
from engine.season.seam.wrappers import sigma
from engine.season.state.carriers import Act, Person, Question
from engine.season.state.gate import WriteClass
from .test_in10_record_operands import _resolve
from .test_rem30_character_sheet import _run

#: The 1-season hashes with the expansion stubbed out (`PYTHONHASHSEED=0`), as of CP-T03-01's `individual` reads in
#: `Event.observed` (the parent tree's, `d5358a9a`, were the previous values: `f2e5e265...`, `0d25717b...`, `05f065f4...`).
#: RE-PINNED ONCE at v10 CP-T03-09 (`capture`, a declared mover of every one-season realm): was `662a7847...`, `af5ba681...`, `6c3e0c17...`.
#: CONTROL: `capture` withheld from the chooser's verbs (in process) reads the old three exactly. A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM.
#: RE-PINNED ONCE at v10 PC-10b (a challenge is a Record; `accept` binds to one; a declared mover wherever a challenge forms):
#: was `7cde746e...`, `971e3d03...`, `0c28be95...`. CONTROL: the base tree (`95f58adb`'s `engine/season`) reads the old three.
#: A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM.
#: RE-PINNED ONCE at v11 CR-87 (violence made exceptional: the build's loyalty rows and `fight`'s contexts, a declared mover
#: of the build and of every season that fought): was `f9c01c27...`, `086d1092...`, `6312b4a1...`. CONTROL:
#: `test_cr87_violence_contexts.py::revert_cr87` reads the pre-item hashes exactly. A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM.
BASE = {
    0: "e9d7c8974bf509ca2b915489cc4f371c",
    1: "9e1bb7c269b7bc1523a342d11d3fcfb0",
    2: "fe7b5f497865689edcd0084d1a1effa7",
}

#: The four Niflhel ids the archived file STRIKES (it prints no row for them): never members.
STRUCK = ("3-NI1", "3-NI2", "3-NI3", "3-NI4")

PLANTED, OTHER = "NPC-087", "NPC-084"                   # two rows that author no lifepath
P_ID, Q_ID = "p_npc_087", "p_npc_084"
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


def test_every_template_names_only_verb_capability_values():
    names = set(VERBS.VOCATIONS)
    held = [k for keys in R.LIFEPATH_TEMPLATES.values() for k in keys]
    assert held and set(held) <= names
    assert any(not keys for keys in R.LIFEPATH_TEMPLATES.values()), "no row maps to none: the cut invented one"


def _cells():
    return R.table("lifepath_templates")


@pytest.mark.parametrize("mutate", [
    lambda c: c["3-CR4"].update(holds=["arms"]),                    # a key outside `verb_capability`'s values
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
        R._load_lifepath_templates(cells, R.LIFEPATHS, set(VERBS.VOCATIONS))


def test_the_shipped_cells_pass_the_same_loader():
    assert R._load_lifepath_templates(_cells(), R.LIFEPATHS, set(VERBS.VOCATIONS)) == R.LIFEPATH_TEMPLATES


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
    w = PO.build_realm(0)
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
    assert sigma.faculty(w, p, "research") == sigma.faculty(w, q, "research") == default
    holders = {pid: x.capability for pid, x in w.persons.items() if x.capability}
    assert holders == {P_ID: {"inquiry": default}, "p_npc_004": {"inquiry": default},
                       "p_npc_088": {"inquiry": default}}, holders


def test_train_on_inquiry_executes_for_the_holder_and_is_refused_for_the_other(planted_world):
    w, d = planted_world
    default = w.fixtures.get("pool_default")
    assert _train(w, d, Q_ID) == ["train.refused"] and w.persons[Q_ID].capability == {}
    assert _train(w, d, P_ID) == ["capability.raised"]
    assert w.persons[P_ID].capability == {"inquiry": default + 1}
    assert sigma.faculty(w, w.persons[P_ID], "research") == default + 1, "the raised key is the pool"


def test_the_lifepath_id_is_stored_nowhere_on_a_person(planted_world):
    w, _d = planted_world
    p = w.persons[P_ID]
    assert LIFEPATH_TO_INQUIRY not in repr(p)
    assert not [f.name for f in dataclasses.fields(Person) if "lifepath" in f.name or "vocation" in f.name]
    assert not any(LIFEPATH_TO_INQUIRY in repr(x) for x in w.persons.values())


# ======================================================================================
# PLANTED FAILURE AND CONTROL
# ======================================================================================

def test_the_planted_failure_the_expansion_skipped_reddens_the_train_assertion(monkeypatch):
    """The assertion above can observe the failure it excludes: with the expansion skipped the planted person
    holds nothing and `train` on `inquiry` is refused, not raised."""
    monkeypatch.setattr(cast, "capability_of", lambda r, pool_default: {})
    w, d = _world(monkeypatch)
    assert w.persons[P_ID].capability == {}
    assert _train(w, d, P_ID) == ["train.refused"] != ["capability.raised"]


@pytest.mark.parametrize("seed", sorted(BASE))
def test_control_the_expansion_skipped_reproduces_the_pre_commit_hash(monkeypatch, seed):
    """With the registry's authored rows in place and the expansion skipped, the 1-season hash is the parent
    tree's: the lifepath id is read and dropped, so a row that maps to nothing moves nothing, and NPC-004's and NPC-088's
    `inquiry` are the whole mover (`test_rem30_character_sheet.PRE_BUILD` carries the moved hash)."""
    monkeypatch.setattr(cast, "capability_of", lambda r, pool_default: {})
    assert _run(PO.build_realm(seed), 1) == BASE[seed]


def test_the_shipped_expansion_is_the_mover_by_the_one_row_that_maps_to_a_key():
    """The same hash with the expansion ON differs from the parent's at seed 0 (the other arm of the control)."""
    assert _run(PO.build_realm(0), 1) != BASE[0]
