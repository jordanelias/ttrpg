"""CR-81 (B10-09 close two, `ED-IN-0318`) -- THE REALM STARTS WITH ACQUAINTANCES. Jordan, 2026-11-04: "many
characters should already know each other based on faction belonging, and high status characters will know
each other (eg Duke Duchess king queen)". The build step is `harness/populated.py::acquaintance_pairs` and
`seed_acquaintances`, run last in `build_realm`; `acquaintances=False` is its control arm.

MEASURED (`PYTHONHASHSEED=0`, this commit's tree against its parent, 67f5b086), the same on seeds 0, 1 and 2:

    persons who know no one at build            83 of 83  ->  41 of 83
    `exists:Person` claims written              236 (226 faction co-member pairs, 10 high-status pairs not
                                                already co-members), the longest ledger at build 12 of `ledger_cap` 200
    persons for whom `tell` forms at build      0  ->  37   (CR-03's reader: every question `questions_for`
                                                delivers him, `opening_set` over `assemble(p, q, 12)`)

THE 41 WHO STILL KNOW NO ONE are the 37 cohorts (no `commit` to a faction, no seat), the 3 cast members
`build_realm` places in no faction (`w._unplaced_cast`), and the one member of the one-member faction
(Schoenland's). Read, not targeted: the test below derives the figure from the two sources and asserts the
pin agrees with it.

[ASSUMPTION; medium; Jordan to correct; revert: delete the build step] each of: "know one another" is mutual
and complete within a faction; the duchy seats are the high-status set with the throne and its consort; the
added claims evict no claim the base keeps. At build every base ledger is empty and none is evicted (the
control test below). ⚠ IN PLAY THE THIRD IS MEASURED FALSE, AND BOUNDED (`seed_acquaintances`' docstring has
the figures): ledgers reach `ledger_cap` in season 1 and a base claim ranking below an acquaintance claim is
evicted while it stays. Against a shadow ledger (the same stream less the acquaintance claims; 0 on the step-off
arm), the base claims displaced at once peak at 93, 142 and 152 on seeds 0-2, never above the 236 written, and
season-1 evictions rise by 90, 139 and 226. The acquaintance claims fade as any build-time claim does: 0, 11 and
0 of 236 still held at season 4. A durable acquaintance would need a carrier eviction does not reach: not ruled,
not built. Not asserted here (a play-time reading, not a build property).
⚠ EVERY PLAY-TIME FIGURE ABOVE IS AT `ledger_cap` 200, NOW THE CONTROL ARM: CR-82 raised the cap to 3200, and
the fade at 200 is re-read there (`test_cr82_ledger_retention.py`; 6 of 236 at season 4 on seed 1 at CR-82's
parent, where this commit read 11). The build-time pins below do not read the cap (12 claims at most per
ledger at build) and do not move.
"""

from __future__ import annotations

import pytest

from ..data.rosters import OFFICES_SEATS
from ..decision import assemble
from ..decision.options import opening_set
from ..harness import populated
from ..harness.populated import build_realm
from ..queries import world_q
from ..queries.person_q import KNOWN_PERSON_CLAIM, known_persons
from ..queries.world_q import faction_holding

SEEDS = (0, 1, 2)
# `build_realm(s, acquaintances=False).content_hash()`, the control arm = the parent tree's build with CR-86's rename and vassals (read 2026-11-05; before CR-86 the PARENT tree 67f5b086 read 70ea49cb... / af5f8b97... / b836647f...): the control arm reproduces them.
PARENT_HASHES = {0: "876820336e2259604acb280ab3452a71", 1: "ca9698d7033f5e106bcc1ec78ba3dd1a",   # CR-86 re-pin: was 70ea49cb... / af5f8b97... / b836647f...
                 2: "c77d3b277f42ec57d3a073dd751287b1"}
KNOW_NONE_AT_BUILD = 41          # of 83, every seed (read, see the docstring)
JORDANS_EXAMPLE = frozenset({"King", "Queen", "Duke", "Duchess"})   # his words, an independent pin on the floor


@pytest.fixture(scope="module")
def worlds():
    return {s: (build_realm(s), build_realm(s, acquaintances=False)) for s in SEEDS}


def _know_none(w) -> int:
    return sum(1 for pid, p in w.persons.items() if not known_persons(p.ledger, pid))


def _expected_pairs(w) -> set:
    """THE PAIRS BY A SECOND ROUTE: faction from the PERSON's end (`faction_holding`, where the build reads
    `members` from the faction's), and the high seats by Jordan's four words over `offices.yaml`'s rows."""
    by_fac: dict = {}
    for pid in w.persons:
        f = faction_holding(w, pid)
        if f is not None:
            by_fac.setdefault(f, []).append(pid)
    high = {next(t.subject for t in w.tenures if t.kind == "hold" and t.live and t.object == row["id"])
            for row in OFFICES_SEATS if row["post"] in JORDANS_EXAMPLE}
    groups = list(by_fac.values()) + [sorted(high)]
    return {(a, b) for g in groups for a in g for b in g if a != b}


def _assert_acquainted(w) -> int:
    """Every expected pair is known, and the know-no-one count is the pin. Returns the pairs checked."""
    pairs = _expected_pairs(w)
    for a, b in sorted(pairs):
        assert b in known_persons(w.persons[a].ledger, a), (a, b)
    reached = {a for a, _ in pairs}
    assert _know_none(w) == len(w.persons) - len(reached) == KNOW_NONE_AT_BUILD, _know_none(w)
    return len(pairs)


def _tell_formers(w) -> int:
    n = 0
    for p in w.persons.values():
        n += any(c.verb == "tell" for q in world_q.questions_for(w, p)
                 for c in opening_set(p, assemble(p, q, 12), q, w.fixtures))
    return n


def test_the_realm_starts_with_acquaintances_on_every_seed(worlds):
    """EXIT: every faction co-member pair and every pair among the high-status seats is known, at build, on
    seeds 0-2; the count of persons who know no one falls from 83 of 83 (the control) to the pin."""
    checked = 0
    for s, (on, off) in worlds.items():
        assert len(on.persons) == len(off.persons) == 83
        assert _know_none(off) == 83
        checked += _assert_acquainted(on)
        assert sorted(on._acquaintances) == sorted(f"c_acq_{a}_{b}" for a, b in _expected_pairs(on))
    assert checked == 3 * 236, checked


def test_the_high_status_set_is_the_throne_its_consort_and_the_duchy_seats(worlds):
    """The floor (`HIGH_STATUS_FLOOR`, by rung kind and title) picks exactly the seats Jordan named."""
    on, _ = worlds[0]
    rows = [r for r in OFFICES_SEATS if r["post"] in JORDANS_EXAMPLE]
    assert {r["post"] for r in rows} == JORDANS_EXAMPLE and len(rows) == 5   # two Dukes (Valorsmark, Varfell)
    holders = {populated._first_holder(on, r["id"]) for r in rows}
    assert len(holders) == 4                     # the King also holds Valorsmark's ducal seat
    for a in holders:
        assert holders - {a} <= set(known_persons(on.persons[a].ledger, a)), a


def test_tell_forms_for_persons_it_formed_for_none(worlds):
    """CR-03's base: `tell` forms for 0 persons at build. With the step it forms for the measured 37."""
    on, off = worlds[0]
    assert _tell_formers(off) == 0
    assert _tell_formers(on) == 37


def test_control_the_step_off_is_the_parent_realm_and_no_base_claim_is_pushed_out(worlds):
    """CONTROL: `acquaintances=False` reproduces the parent tree's hashes; and on every person the arm's
    ledger, less the claims the step wrote, equals the control's claim by claim (none pushed out, none
    altered), every added claim is a truthy `exists:Person` reading, and no ledger exceeds `ledger_cap`."""
    persons = 0
    for s, (on, off) in worlds.items():
        assert off.content_hash() == PARENT_HASHES[s], s
        assert on.content_hash() != PARENT_HASHES[s], s
        cap = on.fixtures.get("ledger_cap")
        added = set(on._acquaintances)
        for pid, p in on.persons.items():
            base = [c for c in p.ledger if c.id not in added]
            assert base == off.persons[pid].ledger, pid
            assert len(p.ledger) <= cap, (pid, len(p.ledger))
            for c in p.ledger:
                if c.id in added:
                    assert c.holder == pid and c.predicate == KNOWN_PERSON_CLAIM["predicate"] and c.value
            persons += 1
    assert persons == 3 * 83


def test_planted_failure_the_step_a_no_op_reproduces_the_base_and_reddens_the_exit(monkeypatch):
    """PLANTED FAILURE: with `seed_acquaintances` writing nothing, 83 of 83 know no one again and the
    exit's own assertion goes red."""
    monkeypatch.setattr(populated, "seed_acquaintances", lambda w, pairs: [])
    w = build_realm(0)
    assert _know_none(w) == 83
    assert w.content_hash() == PARENT_HASHES[0]
    with pytest.raises(AssertionError):
        _assert_acquainted(w)
