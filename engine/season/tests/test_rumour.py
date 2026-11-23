"""B11.09 (`08_FI_02` edits 2-4, `U5c_FI_residue.md` §6) -- THE TELLING'S SLANTS: `unshared` AND `unshared_first`.

`rosters.yaml: said_slants` carries two arms beside `newest` and `valence`. `unshared` never passes on the transport's own kinds (the predicates a
`tell` or a `lie` row emits); `unshared_first` is `unshared` that then picks within the first non-empty tier of `told, inferred, deed, quantity,
other` (`queries/person_q.py::said_of`). The realm tests read the shipped fixtures plus the two arms the item names (`said_slant: unshared_first`,
`telling_hearers: seen_since_move`) against the control (`newest`, `known`), seeds 0-2, two seasons, each (seed, arm) built and played once.

⚠ `test_two_hop_chains_at_two_of_three_seeds` MAY READ RED until `16_PESSIMIST_FI_A` edits 1-3 land (`U5c_FI_residue.md` §2 row 3 names them with the
gate): the batch's `EXPECTED RED UNTIL` line for the second half's item that lands them. A red reading is the item's FALSIFIER reported, not tuned.
"""
from __future__ import annotations

import functools

from ..boot.realm import build_realm
from ..data.fixtures import DEFAULT_FIXTURES
from ..epistemic import SEEN_PREDICATE
from ..harness import populated
from ..queries.person_q import said_of
from ..state.carriers import Claim

SEEDS = (0, 1, 2)
ARM = DEFAULT_FIXTURES.sweep("said_slant", "unshared_first").sweep("telling_hearers", "seen_since_move")


@functools.lru_cache(maxsize=None)
def reading(seed: int, arm: bool) -> dict:
    """`{"two_hop": claims held with a chain of two or more, "told": claims held with a chain, "news_told", "news_untold", "refused": event counts}`
    for the realm at `seed` after two seasons, under the two new arms (`arm`) or the control."""
    w = build_realm(seed, fixtures=ARM if arm else DEFAULT_FIXTURES)
    populated.run(2, seed, w=w)
    held = [c for p in w.persons.values() for c in p.ledger]
    kinds = [e.kind for e in w.log]
    return {"two_hop": sum(1 for c in held if len(c.chain) >= 2), "told": sum(1 for c in held if c.chain),
            "news_told": kinds.count("news.told"), "news_untold": kinds.count("news.untold"), "refused": kinds.count("tell.refused")}


def test_two_hop_chains_at_two_of_three_seeds():
    got = {s: reading(s, True)["two_hop"] for s in SEEDS}
    assert len(got) == 3
    print("TWO-HOP", got)
    assert sum(1 for n in got.values() if n > 0) >= 2, got


def test_control_reads_no_two_hop_chain():
    got = {s: reading(s, False)["two_hop"] for s in SEEDS}
    assert len(got) == 3
    assert set(got.values()) == {0}, got


def test_told_claims_per_news_told_at_least_one():
    checked = 0
    for s in SEEDS:
        r = reading(s, True)
        if r["news_told"]:
            checked += 1
            assert r["told"] / r["news_told"] >= 1, (s, r)
    assert checked >= 1


def test_tell_refused_per_admitted_telling_falls():
    def ratio(arm):
        refused = sum(reading(s, arm)["refused"] for s in SEEDS)
        admitted = sum(reading(s, arm)["news_told"] + reading(s, arm)["news_untold"] for s in SEEDS)
        assert admitted > 0
        return refused / admitted
    control, arms = ratio(False), ratio(True)
    print("REFUSED PER ADMITTED", control, arms)
    assert arms < control, (control, arms)


def test_unshared_never_passes_on_a_transport_kind():
    """A hand-built ledger: the teller's newest claim about HH is the `news.told` the transport deposits, and an older deed. `newest` would retell
    the transport kind; both new arms drop it and pass on the deed. The kinds dropped are every kind a `tell` or `lie` row emits (derived)."""
    from ..data.verbs import DEED_KINDS, VERB_TABLE
    transport = {k for v in ("tell", "lie") for k in (*VERB_TABLE[v].emits, *VERB_TABLE[v].emits_on_refusal)}
    assert "news.told" in transport

    def claim(n, predicate, when, **kw):
        return Claim(f"c{n}", "T", "HH", predicate, kw.pop("value", True), when, kw.pop("source", "firsthand"), 100, "own", 0, **kw)
    deed = sorted(DEED_KINDS - transport)[0]
    ledger = [claim(1, deed, 1), claim(2, "news.told", 5)]
    assert said_of(ledger, "HH", DEFAULT_FIXTURES).predicate == "news.told"          # the control retells the transport
    checked = 0
    for arm in ("unshared", "unshared_first"):
        said = said_of(ledger, "HH", DEFAULT_FIXTURES.sweep("said_slant", arm))
        assert said is not None and said.predicate == deed and said.predicate not in transport, (arm, said)
        checked += 1
    # only transport and sighting: the transport is dropped, the `seen` is the last resort
    seen = claim(3, SEEN_PREDICATE, 6, value=("HH", "somewhere"))
    only = said_of([claim(2, "news.told", 5), seen], "HH", DEFAULT_FIXTURES.sweep("said_slant", "unshared"))
    assert only is not None and only.predicate == SEEN_PREDICATE
    assert said_of([claim(2, "news.told", 5)], "HH", DEFAULT_FIXTURES.sweep("said_slant", "unshared_first")) is None
    assert checked == 2
    # the tiers: what he was told (a chain) outranks a newer deed at `unshared_first` only; `unshared` takes the newest
    told_old = claim(4, "some.reading", 2, chain=("W",))
    newer = claim(5, deed, 4)
    assert said_of([told_old, newer], "HH", DEFAULT_FIXTURES.sweep("said_slant", "unshared_first")).predicate == "some.reading"
    assert said_of([told_old, newer], "HH", DEFAULT_FIXTURES.sweep("said_slant", "unshared")).predicate == deed
