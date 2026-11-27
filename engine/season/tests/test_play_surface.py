"""B34.01 -- THE FOUR GATE TESTS OF THE PLAYER SURFACE, written before the readers they test (`proposals/11_GO_player_surface_contract_B.md`
"Build order and tests" 1; one file, `IS-B3` part 2 §6.1). The §3 own-outcome test is `test_play_surface_own_outcome.py`.

  * `test_transcript_hash_equals_plain_run` (gate 1) -- the transcript `harness/play_surface.py` prints for the seated person ends at the
    `content_hash` of the plain run on the same seed (seeds 0-2, one season): the surface reads and writes nothing. Lands green at B34.04.
  * `test_offer_rows_follow_make_ranker_and_watch_terms` (gate 2) -- for each deliberation, `offer(p, v).rows` is the order `make_ranker`
    gave, and each row's `terms` is what CHAR's `watch` hook reported for it; and a planted claim that changes his belief about ONE subject
    changes `odds` for acts on that subject only. Lands green at B34.02.
  * `test_account_prior_teller_unattributed` (gate 4) -- `account(p, since)` over a hand-built ledger: a told claim reads `own=False` with
    `claim.teller` set, two claims on one cell give the later row a `prior`, an event-kind deposit with no doer reads `unattributed=True`.
    Lands green at B34.03.
  * `test_withheld_rows_are_own_state_only` (gate 5) -- a withheld row names only an own-state conjunct (`OWN_STATE_STEMS`), of a verb whose
    cell asks one; no verb whose requirement is the world's appears. Lands green at B34.02.

EXPECTED RED UNTIL B34.04 (the readers `situation`, `offer`, `account` and the runner's `--seed/--person/--seasons` command do not exist at
this commit): nothing is skipped or marked xfail, so each reddens with an ImportError / a nonzero exit, and the item that builds the
reader turns it green. THE SIGNATURES ARE THE SOURCE'S, VERBATIM: `offer(p, v)` takes no fixtures (its source names none, and
`make_ranker` needs `fx`), so B34.02 reconciles that one call (`_offer`, below) and nothing else.

The planted-claim arm of gate 2 stands a believer's odds in for `View.odds` (a closure over the planted ledger): the claim-to-odds law is
`seam/wrappers/sigma.py::believed_chance`'s and `test_odds_of.py`'s; this arm asks only that `offer` routes the View's answer to the row
of the act it prices, subject by subject.
"""
from __future__ import annotations

import dataclasses
import os
import re
import subprocess
import sys

import pytest

from ..boot.realm import build_realm
from ..data import files
from ..data.requires import OWN_STATE_STEMS
from ..data.verbs import VERB_TABLE
from ..decision.choose import _payload_of, _writing_bands
from ..harness import populated as POP
from ..harness import probes as P
from ..loop.driver import SeasonDriver, resolvable_verbs
from ..queries.person_q import CAPABILITY_CLAIM
from ..state.ids import draw_factory
from ..state.carriers import Act, Claim, Person, View

SEATED = "p_npc_001"


_CHOOSER = {}       # the fixtures and the draw `_deliberations`' chooser was built with: what `offer` is handed (it cannot reach them through `(p, v)`)


def _offer(p, v):
    """The one call of `decision/sheet.py::offer` this file makes: `offer(p, v)` plus the `fx`, `verbs` and `draw` `make_ranker` needs, which are the
    chooser's own (`offer`'s docstring says why the source's two-argument form cannot carry them)."""
    from ..decision.sheet import offer
    return offer(p, v, _CHOOSER["fx"], _CHOOSER["verbs"], _CHOOSER["draw"])


def _deliberations(seed: int, per_person=None, limit: int = 10 ** 9):
    """One season of the plain realm run (`populated.run`'s composition), the chooser built with CHAR's `watch` hook. For each deliberation that
    formed a candidate set, `per_person(p, v, ranked, terms)` is called inside the chooser call, so `v.odds` still closes over the
    barrier's world. Writes nothing the plain run does not. Returns how many deliberations it was called for."""
    w = build_realm(seed)
    d = SeasonDriver(w)
    seen: list = []
    _CHOOSER.update(fx=w.fixtures, verbs=resolvable_verbs(), draw=draw_factory(w.world_seed, lambda: w.tick))

    def hook(p, q, ranked, terms, sampled):
        # `make_ranker` RETURNS the sampled order (`rank`'s value, the order the chooser packs and the player's sheet shows), so a row is read in
        # that order, each with the `terms` the hook reported for the same candidate (`terms` is parallel to `ranked`, which is not the sampled order).
        by = {id(c): t for c, t in zip(ranked, terms)}
        seen.append((list(sampled), [by[id(c)] for c in sampled]))
    real = P.chooser(w, verbs=_CHOOSER["verbs"], watch=hook)
    n = 0

    def choose(p, v, s, ask_budget):
        nonlocal n
        before = len(seen)
        out = real(p, v, s, ask_budget)
        if len(seen) > before and n < limit:
            n += 1
            per_person(p, v, *seen[-1])
        return out
    d.season(choose, question=None, contest_max_depth=w.fixtures.get("contest_max_depth"))
    return n


# -- gate 1 ----------------------------------------------------------------------------------------------------

@pytest.mark.slow
@pytest.mark.parametrize("seed", [0, 1, 2])
def test_transcript_hash_equals_plain_run(seed):
    """GATE 1: `python -m engine.season.harness.play_surface --seed S --person p_npc_001 --seasons 1` exits 0 and its `content_hash` is the plain
    run's (`build_realm(S)`, `populated.run(1, S)`) at the same seed. The CONTROL is the plain run, read in this process on this tree."""
    w = build_realm(seed)
    POP.run(1, seed, w=w)
    plain = w.content_hash()
    env = {**os.environ, "PYTHONHASHSEED": "0"}
    proc = subprocess.run([sys.executable, "-m", "engine.season.harness.play_surface", "--seed", str(seed), "--person", SEATED,
                           "--seasons", "1"], capture_output=True, text=True, cwd=str(files.REPO_ROOT), env=env, timeout=900)
    assert proc.returncode == 0, proc.stderr[-2000:]
    hashes = re.findall(r"content_hash\W+([0-9a-f]{32})", proc.stdout)
    assert hashes, f"the transcript printed no content_hash:\n{proc.stdout[-1500:]}"
    assert hashes[-1] == plain, (seed, hashes[-1], plain)


# -- gate 2 ----------------------------------------------------------------------------------------------------

def test_offer_rows_follow_make_ranker_and_watch_terms():
    """GATE 2, in two arms read in one season of the realm. (a) At each of the first 40 deliberations the order of `Offer.rows` is `make_ranker`'s
    (the order the `watch` hook was handed) and each row's `terms` is what the hook reported for it. (b) At the first deliberation that prices an
    act on one subject and an act on another, one planted claim of his about S moves the `odds` of the rows on S and no other row's. The
    believer of arm (b) is the stand-in the module docstring names: 0.25 for every act, 0.75 for an act on a subject he holds the planted
    claim about."""
    checked, planted = [0], []

    def believer(holder):
        def odds(act, bands):
            named = {c.subject for c in holder.ledger if c.id == "c_plant"}
            return 0.75 if named & set((act.payload or {}).values()) else 0.25
        return odds

    def by(rows):
        out: dict = {}
        for r in rows:
            out.setdefault((r.candidate.verb, r.candidate.subject), set()).add(r.odds)
        return out

    def per_person(p, v, ranked, terms):
        if checked[0] < 40:
            rows = _offer(p, v).rows
            assert [(r.candidate.verb, r.candidate.subject) for r in rows] == [(c.verb, c.subject) for c in ranked], p.id
            assert [tuple(r.terms) for r in rows] == [tuple(t) for t in terms], p.id
            checked[0] += 1
        priced = [c for c in ranked if c.subject is not None and _writing_bands(c) is not None]
        if planted or not priced or all(c.subject == priced[0].subject for c in ranked if c.subject is not None):
            return
        subject = priced[0].subject
        p1 = dataclasses.replace(p, ledger=tuple(p.ledger) + (Claim("c_plant", p.id, subject, CAPABILITY_CLAIM + "argue", 9, 0, "told", 5, "own"),))
        view = lambda who: View(v.holder, list(v.claim_ids), max(len(v.claim_ids), 1), v.question, v.questions, believer(who))
        before, after = by(_offer(p, view(p)).rows), by(_offer(p1, view(p1)).rows)
        assert set(before) == set(after)
        moved = {k for k in before if before[k] != after[k]}
        assert moved and all(k[1] == subject for k in moved), (subject, sorted(moved, key=str))
        assert any(k[1] != subject and before[k] == after[k] for k in before), "no act on another subject was priced to compare"
        planted.append(subject)
    _deliberations(0, per_person)
    assert checked[0] >= 20, f"only {checked[0]} deliberations were read: the hook or the reader did not run"
    assert planted, "no deliberation priced an act on one subject beside an act on another"


# -- gate 4 ----------------------------------------------------------------------------------------------------

def test_account_prior_teller_unattributed():
    """GATE 4 over a hand-built ledger (`account` reads `p`'s own ledger and nothing else): a told claim reads `own=False` with `claim.teller`
    set; two claims on one cell give the later row a `prior` (the earlier one) and the earlier none; an event-kind deposit with no doer reads
    `unattributed=True`, and the same deposit with his own doer does not (it is `own=True`, the echo of his deed)."""
    from ..decision.sheet import account
    p = Person("p_holder")
    told = Claim("c_told", "p_holder", "p_x", "at", "here", 2, "told", 5, "own", chain=("p_teller",))
    old = Claim("c_old", "p_holder", "p_y", "at", "there", 2, "firsthand", 5, "own")
    new = Claim("c_new", "p_holder", "p_y", "at", "elsewhere", 3, "firsthand", 5, "own")
    bare = Claim("c_bare", "p_holder", "p_z", "travel.moved", True, 3, "firsthand", 5, "own")
    done = Claim("c_done", "p_holder", "p_w", "travel.moved", True, 3, "firsthand", 5, "own", doer="p_holder")
    p.ledger.extend([told, old, new, bare, done])
    rows = {r.claim.id: r for r in account(p, (1, 0))}
    assert set(rows) == {"c_told", "c_old", "c_new", "c_bare", "c_done"}, sorted(rows)
    assert rows["c_told"].own is False and rows["c_told"].claim.teller == "p_teller"
    assert rows["c_new"].prior is not None and rows["c_new"].prior.id == "c_old" and rows["c_old"].prior is None
    assert rows["c_bare"].unattributed is True and rows["c_bare"].own is False
    assert rows["c_done"].own is True and rows["c_done"].unattributed is False


# -- gate 5 ----------------------------------------------------------------------------------------------------

def test_withheld_rows_are_own_state_only():
    """GATE 5, over the realm's first season: every `WithheldRow` is of a verb whose `requires_typed` cell asks an own-state stem, and its `unmet`
    names one; so no verb whose requirement is the world's is ever withheld. `checked` is asserted, so a season that withheld nothing is a red
    test and not a vacuous one."""
    checked = [0]

    def per_person(p, v, ranked, terms):
        for r in _offer(p, v).withheld:
            stems = set(VERB_TABLE[r.verb].requires_typed.stems()) if VERB_TABLE[r.verb].requires_typed is not None else set()
            own = stems & OWN_STATE_STEMS
            assert own, (p.id, r.verb, "withheld, but its cell asks no own-state stem", sorted(stems))
            assert any(s in r.unmet for s in own), (p.id, r.verb, r.unmet, sorted(own))
            checked[0] += 1
    _deliberations(0, per_person)
    assert checked[0] >= 1, "no row was withheld at the realm's first season: the gate observed nothing"
