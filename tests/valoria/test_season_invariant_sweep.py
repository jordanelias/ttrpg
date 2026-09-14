"""M1 row 5 — "N seeds, zero invariant violations" — and the falsifier for every predicate it runs.

`engine/season/harness/invariants.py` is the single owner of what a season must not have done;
this file is the evidence that each of its predicates can actually OBSERVE the failure it
excludes (`CLAUDE.md` §0.1 pt 2 — `pytest.approx` on an exactness claim is "not a weak test but
an absent one"), and §0.1 pt 3's named falsifier for the sweep as a whole.

⚠⚠ **WHY A MUTATION PER PREDICATE RATHER THAN "IT RETURNS [] ON A HEALTHY WORLD".** A sweep that
reports zero is indistinguishable from a sweep that looks at nothing, and this module's first
writing proved the failure runs the other way too: an entity set missing `w.records` reported
**176 violations across 24 seeds**, 136 of them manufactured by the predicate rather than found
in the engine. So each predicate is broken deliberately here and must fire, and
`test_the_entity_set_covers_every_world_collection_a_tenure_can_name` pins the set against
`World`'s own `__init__` so the over-firing direction cannot come back either.
"""
import os
import sys

import pytest

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, REPO_ROOT)

from engine.season.harness import headless, invariants as I   # noqa: E402
from engine.season.state.carriers import (                    # noqa: E402
    Claim, Event, Office, Proposition, Tenure)

SWEEP_SEEDS = 12          # headless is ~0.13s/season measured; 12 seeds keeps this a unit test
PROBE_SEED = 20260819     # the fixed-seed convention tools/m1_acceptance.py uses


def _world(seed=PROBE_SEED, seasons=1):
    return headless.run(seasons=seasons, seed=seed)["world"]


# ── the sweep itself ────────────────────────────────────────────────────────────────────────

def test_the_sweep_examines_every_invariant_on_every_seed():
    """`checked` is the anti-vacuity term: zero violations must be a result, not an empty loop."""
    r = I.sweep(lambda s: _world(s), range(SWEEP_SEEDS))
    assert r["seeds"] == SWEEP_SEEDS
    assert r["checked"] == SWEEP_SEEDS * len(I.INVARIANTS), (
        f"{r['checked']} checks over {r['seeds']} seeds, expected "
        f"{SWEEP_SEEDS * len(I.INVARIANTS)}. A sweep reporting no violations while running fewer "
        "checks than it claims is the shape `checked` exists to make visible")


def test_every_declared_exception_carries_a_citation_and_still_fires():
    """A declared exception is a KNOWN violation, never a silenced one.

    Both halves matter. The citation stops `DECLARED` becoming a rug — an entry with no `ED-`/`F`
    reference is someone quieting a finding. And the predicate must still FIRE on the declared
    case: `sweep` routes it to `declared` rather than dropping it, so the count stays visible.
    """
    assert I.DECLARED, "DECLARED is empty — headless.py's prop_einhir should still be in it"
    for (inv, ident), cite in I.DECLARED.items():
        assert inv in I.INVARIANTS, f"{inv!r} declares an exception to no known invariant"
        assert "ED-" in cite or "F8" in cite, (
            f"the exception for {ident!r} cites nothing. A declared exception without a register "
            "reference is a silenced finding")
    r = I.sweep(lambda s: _world(s), range(SWEEP_SEEDS))
    assert r["declared"], (
        "no declared violation fired. prop_einhir is an authored fixture in headless.py, so it is "
        "present every run — an empty `declared` means the predicate stopped seeing it")


def test_the_entity_set_covers_every_world_collection_a_tenure_can_name():
    """Pinned against `World.__init__`, because the first writing missed `w.records`.

    THE FAILURE THIS EXCLUDES IS OVER-FIRING, which is the opposite direction from the rest of
    this file and is the one that actually happened: with `records` missing, every legitimate
    `hold` on a deed read as a dangling reference and the sweep reported 176 violations, 136 of
    them invented. A collection added to `World` later and not added to `_entities` would do it
    again, silently, to whatever names the new carrier.
    """
    w = _world()
    named = {"persons", "rungs", "offices", "sites", "records",
             "propositions", "dates", "petitions", "dispensations"}
    for coll in named:
        assert hasattr(w, coll), f"World has no {coll!r} — _entities names a collection that is gone"
    # Everything a live Tenure actually names in a real run must be inside the set.
    ents = I._entities(w)
    for t in I._all_tenures(w):
        if t.live and t.kind != "contain":
            assert t.object in ents or t.subject in ents, (
                f"live {t.kind} {t.id!r} names neither end inside the entity set — the set is "
                "narrower than the carriers the loop actually uses")


# ── one mutation per predicate: each must OBSERVE its own defect ────────────────────────────

def _break_tenure_interval(w):
    w.add_tenure(Tenure("mut_interval", "p_carin", "p_carin", "oblige", 5, until=2))

def _break_tenure_referent(w):
    w.add_tenure(Tenure("mut_ref", "p_carin", "nothing_named_this", "hold", 0))

# ⚠ `["ROOT"]`, NOT `[]` — `Event.__post_init__` refuses an empty `causes` (S19.4:
# "[ROOT] makes the empty list unrepresentable rather than merely discouraged"). The
# mutation must build a WELL-FORMED Event that violates the invariant under test and
# nothing else, or it proves the constructor works instead of the predicate.
def _break_log_ids_unique(w):
    e = w.log[0]
    w.log.append(Event(e.id, e.kind, e.subject, [], ["ROOT"], e.emitted_at))

def _break_log_not_from_the_future(w):
    w.log.append(Event("mut_future", "probe", "p_carin", [], ["ROOT"], w.tick + 9))

def _break_claim_not_from_the_future(w):
    p = next(iter(w.persons.values()))
    p.ledger.append(Claim("mut_claim", p.id, p.id, "saw", True, w.tick + 9, "firsthand", 3, "public"))

def _break_body_in_range(w):
    next(iter(w.persons.values())).body = -1

def _break_stance_row_shape(w):
    next(iter(w.persons.values())).stance.append(("p_carin", 99, 99))

def _break_ought_names_an_entity(w):
    w.propositions["mut_ought"] = Proposition("mut_ought", "OUGHT", "no_such_thing", "x", True, 0)

def _break_office_singly_held(w):
    w.offices["mut_seat"] = Office("mut_seat", "Probe Seat", None, ["issue"], faction="Crown")
    w.add_tenure(Tenure("mut_hold_a", "p_carin", "mut_seat", "hold", 0))
    w.add_tenure(Tenure("mut_hold_b", "p_other", "mut_seat", "hold", 0))


MUTATIONS = [
    ("tenure_interval", _break_tenure_interval),
    ("tenure_referent", _break_tenure_referent),
    ("log_ids_unique", _break_log_ids_unique),
    ("log_not_from_the_future", _break_log_not_from_the_future),
    ("claim_not_from_the_future", _break_claim_not_from_the_future),
    ("body_in_range", _break_body_in_range),
    ("stance_row_shape", _break_stance_row_shape),
    ("ought_names_an_entity", _break_ought_names_an_entity),
    ("office_singly_held", _break_office_singly_held),
]


def test_every_invariant_has_a_mutation(  ):
    """No predicate ships without a falsifier, and none is falsified by a stale name."""
    covered = {name for name, _ in MUTATIONS}
    assert covered == set(I.INVARIANTS), (
        f"mutation coverage != the roster. missing: {sorted(set(I.INVARIANTS) - covered)}; "
        f"stale: {sorted(covered - set(I.INVARIANTS))}")


@pytest.mark.parametrize("name,mutate", MUTATIONS, ids=[n for n, _ in MUTATIONS])
def test_the_predicate_observes_its_own_defect(name, mutate):
    """Break the world one way; THAT predicate must fire, and it must name the right invariant."""
    w = _world()
    before = [v for v in I.CHECKS[name](w)]
    mutate(w)
    after = I.CHECKS[name](w)
    assert len(after) > len(before), (
        f"{name} did not fire after its own mutation ({len(before)} -> {len(after)}). A predicate "
        "that cannot observe the defect it names is not a weak check but an absent one")
    assert all(m.startswith(name + ":") for m in after), (
        f"{name} produced a message attributed to another invariant: {after}")


def test_a_broken_world_reaches_the_sweeps_violation_list():
    """The predicates firing is not enough — `sweep` must surface them as NEW, not swallow them."""
    def build(seed):
        w = _world(seed)
        _break_body_in_range(w)
        return w
    r = I.sweep(build, range(3))
    assert len(r["violations"]) >= 3, (
        f"3 broken worlds produced {len(r['violations'])} violations. `sweep` is dropping what the "
        "predicates found — the path from predicate to report is where a silent zero would hide")
