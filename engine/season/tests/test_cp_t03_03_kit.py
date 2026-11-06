"""CP-T03-03 -- KIT REACHES THE FIGHT (`-08` AM-C-04; T03 home §2).

A person's kit, `(weapon, armor)`, is `world_q.kit_of`: per Combatant field, the highest-ranked arms kind
(`rosters.yaml: arms_kinds`) with a positive count in the stores of the rungs he `hold`s, else of his `reside` rung, else
the Combatant's own default. `combat_input` fills `PersonalCombatInput.kits` for BOTH parties in `claimants` order and
`modules/combat/fight.py` passes each to `Combatant(..., weapon=, armor=)`. `arms_kinds` is validated AT LOAD against the
`kit` section of `engine/engine_params/combat_engine_v1.json` (`tools/export_engine_params.py --check`), read by
`engine/substrate/combat_kit.py`, so no key list is copied into `rosters.yaml`.

⚠ THE SHIPPED ROSTERS ARE EMPTY (the inventory is Jordan's content: `-08` AM-C-04). Every test below that needs an arms
kind PLANTS one (`monkeypatch` on `world_q.ARMS_KINDS`, a hand-built world per P9), and the shipped state is its own
control: with no kind `kit_of` is the default for everyone and `build_realm`'s world is the world without the seeding step.

  FALSIFIER: `kit_of` on a holder of a stocked rung returns the roster's top-ranked kind per field; at stock 0 the
  default; a seeded `fight` (real seam, n = 400) with the SUBJECT's holding stocked with the top armour fells the actor at
  the home's rate (T03 §3: 97.5 %) within sampling; the loader refuses an `arms_kinds` key the export does not carry, and
  the exporter's `--check` fails on a drifted `kit` section.
  MUTATION (`test_mutation_...`): read the ACTOR's kit for both parties and the asymmetry vanishes, so the SAME predicate
  that passes on the shipped `combat_input` fails on the mutant.
"""
from __future__ import annotations

import dataclasses
import importlib.util
import json
import random
from pathlib import Path
from unittest import mock

import pytest

from engine.substrate import combat_kit, pc_engine

from ..data.rosters import ARMS_AT_BUILD, ARMS_KINDS, _check_arms_at_build, _check_arms_kinds
from ..gaps import Unspecified
from ..harness import populated, probes as P
from ..loop.driver import SeasonDriver
from ..queries import world_q
from ..seam.wrappers import combat
from ..seam.wrappers._entry import entry_for
from ..state.carriers import Rung, Tenure

ACTOR, SUBJECT = "p_low", "p_mid"            # tiny_world: both reside at the hearth `Hh`
N = 400                                      # the falsifier's fights (the home's n)
HOME_RATE = 0.975                            # T03 §3: a plated subject fells the actor in 97.5 % of fights
# [JUSTIFIED: a 4-sigma band on a binomial share at n = 400 and p = 0.975 (sigma 0.0078), rounded up; sampling, not a tuned figure]
TOL = 0.04

_REPO = Path(__file__).resolve().parents[3]


def _kinds(armor_key="heavy", weapon_key=None):
    """A planted roster, validated by the shipped loader against the real export: two armour kinds (a top and a lower)
    and one weapon kind. Returns `{kind: (field, key, rank)}`."""
    weapon_key = weapon_key or sorted(combat_kit.WEAPONS - {combat_kit.DEFAULTS["weapon"]})[0]
    raw = {"t_plate": dict(field="armor", key=armor_key, rank=3),
           "t_gambeson": dict(field="armor", key="medium", rank=1),
           "t_blade": dict(field="weapon", key=weapon_key, rank=1)}
    return _check_arms_kinds(raw, set(raw), combat_kit.FIELDS)


@pytest.fixture(autouse=True)
def _module_entries():
    """The registrar fills the combat module entry at driver construction (`entry_for` refuses before it)."""
    SeasonDriver(P.tiny_world())


@pytest.fixture
def armed(monkeypatch):
    monkeypatch.setattr(world_q, "ARMS_KINDS", _kinds())


def _world():
    """`tiny_world` plus an ARSENAL the SUBJECT holds (stocked) and the actor does not: the hearth `Hh` where both
    live stays empty, so only the subject's holding carries arms."""
    w = P.tiny_world()
    w.rungs["Arsenal"] = Rung("Arsenal", "hearth", stores={"t_plate": 1})
    w.add_tenure(Tenure("t_hold_arsenal", SUBJECT, "Arsenal", "hold", since=0))
    return w


# ---------------------------------------------------------------------------------------------------------------
# 1 -- THE EXPORT AND THE LOADER
# ---------------------------------------------------------------------------------------------------------------

def test_the_export_is_the_engines_own_keys_and_default_kit():
    engine = pc_engine.load()
    import vocabulary, weapons    # the flat modules `pc_engine.load()` put on the path
    assert combat_kit.WEAPONS == frozenset(weapons.WEAPONS) and len(combat_kit.WEAPONS) > 10
    assert combat_kit.ARMOUR_TIERS == vocabulary.ARMOUR_TIERS == {"none", "light", "medium", "heavy"}
    c = engine.combatant.Combatant("x")
    assert combat_kit.DEFAULTS == {"weapon": c.weapon, "armor": c.armor}, "the default kit is the Combatant's own"
    assert combat_kit.DEFAULTS["weapon"] in combat_kit.WEAPONS and combat_kit.DEFAULTS["armor"] in combat_kit.ARMOUR_TIERS


def _exporter():
    spec = importlib.util.spec_from_file_location("export_engine_params_cp_t03_03", _REPO / "tools" / "export_engine_params.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_the_exporters_check_passes_and_fails_on_a_drifted_kit_section(tmp_path):
    ex = _exporter()
    assert ex.main(["--check"]) == 0, "the committed export no longer matches the oracle"
    drifted = json.loads(Path(ex.OUT_PATH).read_text(encoding="utf-8"))
    drifted["sections"]["kit"]["weapons"].remove("arming")        # a key the engine has, the export lost
    out = tmp_path / "combat_engine_v1.json"
    out.write_text(ex.render(drifted), encoding="utf-8")
    with mock.patch.object(ex, "OUT_PATH", str(out)):
        assert ex.main(["--check"]) == 1, "--check passed on an export that dropped a weapon key"


@pytest.mark.parametrize("raw, why", [
    (dict(field="armor", key="adamantine", rank=1), "a key the export does not carry"),
    (dict(field="armor", key="arming", rank=1), "a weapon key on the armour field"),
    (dict(field="weapon", key="heavy", rank=1), "an armour tier on the weapon field"),
    (dict(field="head", key="arming", rank=1), "a field no Combatant kit has"),
    (dict(field="armor", key="heavy", rank="1"), "a rank that is not a whole number"),
    (dict(field="armor", key="heavy", rank=True), "a rank that is a bool"),
    (dict(field="armor", key="heavy"), "no rank"),
    (dict(field="armor", key="heavy", rank=1, extra=2), "a field the row does not declare"),
])
def test_the_loader_refuses_a_malformed_arms_kind(raw, why):
    with pytest.raises(Unspecified):
        _check_arms_kinds({"k": raw}, {"k"}, combat_kit.FIELDS)


def test_the_loader_refuses_an_unregistered_kind_and_a_tied_rank_and_accepts_a_good_row():
    good = dict(field="armor", key="heavy", rank=2)
    with pytest.raises(Unspecified):                                   # not a `matter_kinds` member
        _check_arms_kinds({"k": good}, {"grain"}, combat_kit.FIELDS)
    with pytest.raises(Unspecified):                                   # two kinds of one field at one rank
        _check_arms_kinds({"a": good, "b": dict(good, key="medium")}, {"a", "b"}, combat_kit.FIELDS)
    ok = _check_arms_kinds({"a": good, "b": dict(good, field="weapon", key="arming")}, {"a", "b"}, combat_kit.FIELDS)
    assert ok == {"a": ("armor", "heavy", 2), "b": ("weapon", "arming", 2)}, "equal ranks across DIFFERENT fields are fine"


def test_the_loader_refuses_a_seed_that_names_no_arms_kind_or_no_rung_kind_or_no_amount():
    kinds = _kinds()
    assert _check_arms_at_build({"hearth": {"t_plate": 2}}, ["hearth", "realm"], kinds) == {"hearth": {"t_plate": 2}}
    for bad in ({"hearth": {"grain": 2}},          # not an arms kind
                {"barn": {"t_plate": 2}},          # not a rung kind
                {"hearth": {"t_plate": 0}},        # not a positive amount
                {"hearth": {"t_plate": True}},     # a bool is not an amount
                {"hearth": {}}):                   # a seed of nothing
        with pytest.raises(Unspecified):
            _check_arms_at_build(bad, ["hearth", "realm"], kinds)


# ---------------------------------------------------------------------------------------------------------------
# 2 -- kit_of
# ---------------------------------------------------------------------------------------------------------------

def test_kit_of_a_holder_of_a_stocked_rung_is_the_top_ranked_kind_per_field_and_the_default_at_stock_zero(armed):
    w = _world()
    default = (combat_kit.DEFAULTS["weapon"], combat_kit.DEFAULTS["armor"])
    assert world_q.kit_of(w, ACTOR) == default, "the actor holds nothing and his hearth is empty"
    assert world_q.kit_of(w, SUBJECT) == (default[0], "heavy"), "armour only: no weapon kind is stocked"
    w.rungs["Arsenal"].stores = {"t_plate": 1, "t_gambeson": 5, "t_blade": 1}
    blade = world_q.ARMS_KINDS["t_blade"][1]
    assert world_q.kit_of(w, SUBJECT) == (blade, "heavy"), "t_plate (rank 3) outranks t_gambeson (rank 1) despite the count"
    w.rungs["Arsenal"].stores = {"t_plate": 0, "t_gambeson": 5, "t_blade": 0}
    assert world_q.kit_of(w, SUBJECT) == (default[0], "medium"), "a zero count is not held; the lower kind is"
    w.rungs["Arsenal"].stores = {"t_plate": 0, "t_gambeson": 0}
    assert world_q.kit_of(w, SUBJECT) == default, "stock 0 is the default"
    w.rungs["Arsenal"].stores = {}
    assert world_q.kit_of(w, SUBJECT) == default


def test_kit_of_reads_his_holdings_and_only_then_his_residence(armed):
    w = P.tiny_world()
    default = (combat_kit.DEFAULTS["weapon"], combat_kit.DEFAULTS["armor"])
    w.rungs["Hh"].stores = {"t_plate": 1}
    assert world_q.kit_of(w, ACTOR) == (default[0], "heavy"), "no holdings: the rung he resides in"
    w.rungs["Arsenal"] = Rung("Arsenal", "hearth", stores={})
    w.add_tenure(Tenure("t_hold_empty", ACTOR, "Arsenal", "hold", since=0))
    assert world_q.kit_of(w, ACTOR) == default, "he holds a rung, so the residence is no second store"
    w.rungs["Arsenal"].stores = {"t_gambeson": 1}
    assert world_q.kit_of(w, ACTOR) == (default[0], "medium")
    assert world_q.kit_of(w, "no_such_person") == default


def test_kit_of_writes_no_store(armed):
    w = _world()
    before = {rid: dict(r.stores or {}) for rid, r in w.rungs.items()}
    for _ in range(3):
        world_q.kit_of(w, SUBJECT)
    assert {rid: dict(r.stores or {}) for rid, r in w.rungs.items()} == before, "a kit is read, never consumed"


# ---------------------------------------------------------------------------------------------------------------
# 3 -- THE FIGHT, THROUGH THE REAL SEAM
# ---------------------------------------------------------------------------------------------------------------

def _actor_felled_share(w, n=N, seed=7):
    """The share of `n` fights, from the input `combat_input` builds for `fight`, in which the ACTOR is felled and the
    subject is not, through the registered module entry (the seam's own), read off the trackers."""
    entry, refusal = entry_for(combat._PRIZE, combat._PROVIDER)
    assert entry is not None, refusal
    inp = combat.combat_input(w, [ACTOR, SUBJECT], "fight")
    rng = random.Random(seed)
    felled = 0
    for _ in range(n):
        ws = entry.fn(inp, rng)["wound_state"]
        felled += bool(ws[ACTOR]["felled"]) and not bool(ws[SUBJECT]["felled"])
    return felled / n


def _asymmetry_holds(w):
    """THE FALSIFIER'S PREDICATE, shared by the shipped seam and its mutant: the plated subject fells the actor at the
    home's rate, and the same pair without the plate does not."""
    armed_share = _actor_felled_share(w)
    bare = _world(); bare.rungs["Arsenal"].stores = {}
    control = _actor_felled_share(bare)
    assert abs(armed_share - HOME_RATE) <= TOL, f"actor felled {armed_share:.3f}, the home's rate is {HOME_RATE}"
    assert control < 0.6, f"the unarmed pair is a coin toss, not {control:.3f}"
    return armed_share, control


def test_a_plated_subject_fells_the_actor_at_the_homes_rate_and_the_unplated_pair_does_not(armed):
    armed_share, control = _asymmetry_holds(_world())
    assert armed_share - control > 0.35, (armed_share, control)


def test_combat_input_carries_a_kit_per_party_in_claimants_order(armed):
    w = _world()
    inp = combat.combat_input(w, [ACTOR, SUBJECT], "fight")
    assert inp.claimants == (ACTOR, SUBJECT) and len(inp.kits) == 2
    assert inp.kits[0] == (combat_kit.DEFAULTS["weapon"], combat_kit.DEFAULTS["armor"])
    assert inp.kits[1] == (combat_kit.DEFAULTS["weapon"], "heavy")
    swapped = combat.combat_input(w, [SUBJECT, ACTOR], "fight")
    assert swapped.kits == (inp.kits[1], inp.kits[0]), "the kit follows the person, not the side"


def test_the_sampler_fight_estimate_builds_the_same_input_so_kits_reach_it(armed):
    w = _world()
    est = combat.fight_estimate(w, ACTOR, None, SUBJECT, "fight")
    assert est["status"] == "ESTIMATED" and est["samples"] == w.fixtures.get("estimate_samples")
    assert est["actor_felled"] > 0.9, est
    bare = _world(); bare.rungs["Arsenal"].stores = {}
    assert combat.fight_estimate(bare, ACTOR, None, SUBJECT, "fight")["actor_felled"] < 0.6


def test_a_record_built_without_kits_is_fought_at_the_engines_default():
    entry, _ = entry_for(combat._PRIZE, combat._PROVIDER)
    w = P.tiny_world()
    inp = combat.combat_input(w, [ACTOR, SUBJECT], "fight")
    plain = dataclasses.replace(inp, kits=())
    default = dataclasses.replace(inp, kits=((combat_kit.DEFAULTS["weapon"], combat_kit.DEFAULTS["armor"]),) * 2)
    for seed in range(5):
        a = entry.fn(plain, random.Random(seed))
        b = entry.fn(default, random.Random(seed))
        assert (a["result"], a["ends"], a["wound_state"]) == (b["result"], b["ends"], b["wound_state"])


def test_mutation_reading_the_actors_kit_for_both_parties_loses_the_asymmetry(armed, monkeypatch):
    """Run in the test: the SAME predicate that passes on the shipped seam FAILS when `combat_input` asks the actor's kit
    of both parties. A predicate that survives the mutant observes nothing."""
    w = _world()
    assert _asymmetry_holds(w)                                         # the shipped seam
    monkeypatch.setattr(combat, "kit_of", lambda world, pid: world_q.kit_of(world, ACTOR))
    with pytest.raises(AssertionError):
        _asymmetry_holds(_world())


# ---------------------------------------------------------------------------------------------------------------
# 4 -- THE CONTROL: EMPTY ROSTERS ARE TODAY'S WORLD
# ---------------------------------------------------------------------------------------------------------------

def test_the_shipped_rosters_are_empty_so_every_person_fights_at_the_default():
    assert ARMS_KINDS == {} and ARMS_AT_BUILD == {}, "the inventory is Jordan's: nothing is authored here"
    w = populated.build_realm(0)
    default = (combat_kit.DEFAULTS["weapon"], combat_kit.DEFAULTS["armor"])
    checked = 0
    for pid in w.persons:
        assert world_q.kit_of(w, pid) == default
        checked += 1
    assert checked > 50, "the control must have observed a populated realm"


def test_seeding_with_no_arms_changes_nothing_and_seeding_arms_moves_the_hash(monkeypatch):
    base = populated.build_realm(0)
    with mock.patch.object(populated, "seed_arms", lambda w, seeds=None: 0):
        unseeded = populated.build_realm(0)
    assert base.content_hash() == unseeded.content_hash(), "the empty `arms_at_build` is the build without the step"
    assert populated.seed_arms(base, {}) == 0
    assert base.content_hash() == unseeded.content_hash()
    n = populated.seed_arms(base, {"settlement": {"t_plate": 2}})
    assert n > 0 and base.content_hash() != unseeded.content_hash(), "a party that holds arms is a hash mover"
    seeded = [r for r in base.rungs.values() if (r.stores or {}).get("t_plate")]
    assert len(seeded) == n and all(r.kind == "settlement" and r.stores["t_plate"] == 2 for r in seeded)
