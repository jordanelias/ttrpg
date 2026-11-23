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


# ---- B11.10 (`08_FI_02` edits 7-8): WHAT IS TOLD AND WHETHER IT IS CONFIDED ARE THE TELLER'S CHOICES -----------------------------------------
CHOICES = DEFAULT_FIXTURES.sweep("said_choices", 3)


def _best_said(w, p, subject):
    """`(what `p` would pass on about `subject`, whether that is not the claim his slant ranks first)` to the first person he could tell it to: the best-scored
    `tell` Candidate (not in confidence), by the chooser's own score; `None` where he has nothing to say."""
    from ..decision.choose import deliberation_memo, score_terms, score_total
    from ..decision.options import opening_set
    from ..state.carriers import Question, View
    q = Question("q_b11_10", "claim_landed", (subject,), "")
    cands = [c for c in opening_set(p, View(p.id, [], w.fixtures.get("view_k"), q), q, w.fixtures)
             if c.verb == "tell" and c.subject == subject and not c.operands.get("in_confidence")]
    if not cands:
        return None
    to = cands[0].operands["to"]
    memo = deliberation_memo(p, w.fixtures)
    best = max((c for c in cands if c.operands["to"] == to), key=lambda c: score_total(score_terms(p, c, w.fixtures, memo, None, q)))
    return best.operands["said"], "said_rank" in best.operands and best.operands["said_rank"] > 0


def test_two_persons_with_the_same_claims_tell_different_claims():
    """At `said_choices` 3, seeds 0-2, one season: persons who hold the same claims about one subject, and differ in what they pursue, do not all tell the
    same claim -- the claim is ranked by `deed_valence` under each teller's own pursuits (`decision/choose.py::choice_lean`)."""
    checked = differing = 0
    for seed in SEEDS:
        w = build_realm(seed, fixtures=CHOICES)
        populated.run(1, seed, w=w)
        held: dict = {}
        for p in w.persons.values():
            about: dict = {}
            for c in p.ledger:
                about.setdefault(c.subject, set()).add((c.predicate, c.value, c.chain))
            for subject, claims in about.items():
                if subject != p.id and len({k[0] for k in claims}) >= 2:
                    held.setdefault((subject, frozenset(claims)), []).append(p)
        for (subject, _), group in held.items():
            if len(group) < 2:
                continue
            got = [_best_said(w, p, subject) for p in group]
            got = [g for g in got if g is not None]
            if len(got) >= 2:
                checked += 1
                # different claims, and at least one is a pick the teller's pursuits made over his slant's first (a claim of lower rank): ranking by valence, not by order
                differing += len({(s.predicate, s.value, s.chain) for s, _ in got}) > 1 and any(moved for _, moved in got)
    print("SAME CLAIMS", checked, differing)
    assert checked >= 1
    assert differing >= 1, (checked, differing)


def test_in_confidence_on_the_act_decides_the_circle():
    """`loop/witness.py::_circle_of` reads the telling's own `in_confidence` where it drew on `telling_privacy` (`08_FI_02` edit 8): True makes the circle at the
    control share 0, False makes none at share 1.0 and takes no draw, and a telling that carries none is the share's as before. The break path itself
    (`confidence.broken` on a retelling outside the circle, the privacy arm) is `test_told_by_channel.py`'s `test_g6_*`."""
    from ..harness import probes as P
    from ..loop.witness import _circle_of
    from ..state.carriers import Act
    w = P.tiny_world()

    def circle(rate, **own):
        act = Act("a_b11_10", "p_low", "tell", payload={"subject": "Hh", "to": "p_mid", **own})
        return _circle_of(w, act, rate)
    checked = 0
    for rate, own, want in ((0.0, {"in_confidence": True}, ("p_low", "p_mid")), (1.0, {"in_confidence": False}, None),
                            (1.0, {}, ("p_low", "p_mid")), (0.0, {}, None)):
        assert circle(rate, **own) == want, (rate, own)
        checked += 1
    assert checked == 4
