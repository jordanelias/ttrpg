"""B34.01 -- THE GATE TESTS OF THE PLAYER SURFACE (`proposals/11_GO_player_surface_contract_B.md` "Build order and tests" 1; one file, `IS-B3` part 2 §6.1), and the later
B34 items' tests below them. The §3 own-outcome test is `test_play_surface_own_outcome.py`.

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

THE READERS EXIST (`situation`, `offer`, `account`, and the runner's `--seed/--person/--seasons` command). `offer` takes the `fx`, `verbs` and `draw` `make_ranker`
needs beside `(p, v)` (its source's two-argument form had no way to reach them), so this file's one call of it is `_offer`, below.

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


def _deliberations(seed: int, per_person=None, limit: int = 10 ** 9, overlay=None):
    """One season of the plain realm run (`populated.run`'s composition), the chooser built with CHAR's `watch` hook. For each deliberation that
    formed a candidate set, `per_person(p, v, ranked, terms)` is called inside the chooser call, so `v.odds` still closes over the
    barrier's world. Writes nothing the plain run does not. Returns how many deliberations it was called for. `overlay(w)` is called once on the
    built world before the first season (a `Fixtures` sweep, as `scenarios.run`'s `on_build`)."""
    w = build_realm(seed)
    if overlay is not None:
        overlay(w)
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


def test_printed_offer_is_the_order_and_terms_the_chooser_ranked():
    """`deliberation_lines`' `[i]` rows are what the chooser ranks: the order and the terms of the `PersonInterior` DELIBERATE builds (his claims read at the tick), not of
    the stored `Person` (whose claims read unfaded). The seed-0 realm is opened at tick 3 and, at the first deliberation, a refusal of one of the verbs it remembers one for
    (`emits_on_refusal`, on the row with the largest pursuit term, so the change survives the print's two decimals) is planted in his ledger at tick 2, so the claim reads faded (one season) in the interior and unfaded in the person.
    The printed rows are then read against the ranker's own over that interior. CONTROL: the planted row's pursuit term is not what it was before the plant."""
    from ..decision.choose import make_ranker
    from ..decision.sheet import development_space
    from ..harness import play_surface as PS
    from ..state.carriers import interior_of
    built, checked = [], [0]

    def per_person(p, v, ranked, terms):
        w, fx, verbs, draw = built[0], _CHOOSER["fx"], _CHOOSER["verbs"], _CHOOSER["draw"]
        c, before = max(((c, t) for c, t in zip(ranked, terms) if VERB_TABLE[c.verb].emits_on_refusal and c.subject), key=lambda ct: abs(ct[1][0]))
        w.persons[p.id].ledger.append(Claim("c_refused", p.id, c.subject, VERB_TABLE[c.verb].emits_on_refusal[0], True, 2, "firsthand",
                                            fx.get("confidence_default"), "own", 0, doer=p.id))
        me = interior_of(w.persons[p.id], w.tick, fx.claim_decay())
        seen: list = []
        order = make_ranker(fx, verbs, draw, lambda _p, _q, r, t, s: seen.append(({id(x): y for x, y in zip(r, t)}, s)))(me, v)
        by, sampled = seen[-1]
        got: list = []
        development_space(fx, lambda who, verb, subj: f"{who}:{verb}:{subj}", lambda sheet: (got.append(sheet), [])[1], verbs, draw)(me, v, None, lambda: 5)
        rows = [ln for ln in PS.deliberation_lines(w, got[0], verbs) if re.match(r"   \[\d+\] ", ln)]
        assert len(rows) == len(sampled), p.id
        for i, (ln, x) in enumerate(zip(rows, sampled)):
            assert ln.startswith(f"   [{i}] {x.verb} {x.subject or ''}".rstrip()) and " ".join(f"{n} {t:+.2f}" for n, t in zip(PS.TERM_NAMES, by[id(x)])) in ln, (p.id, ln)
            if (x.verb, x.subject) == (c.verb, c.subject):
                assert by[id(x)][0] != before[0], "the planted refusal did not move the pursuit term: the arm observed nothing"
                checked[0] += 1

    def at_tick_three(w):
        w.tick = 3
        built.append(w)
    _deliberations(0, per_person, limit=1, overlay=at_tick_three)
    assert checked[0] == 1


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


# -- B34.16: the player is shown all his questions ----------------------------------------------------------------

def test_development_space_ranks_for_the_picked_question():
    """B34.16 (`01_CORE` edit 5). The sheet is shown the player's questions (`Situation.asked`) and `development_space(..., ask=)` takes his pick of one. Read at the
    realm's first season under `question_aggregation_rule` `all`, the one arm whose candidate set holds a row for a later question (under the shipped `first` the
    set forms on the head question alone, so a later question has no row to rank first and the arm would read nothing). At each of the first 40 deliberations that ask two or more
    questions: (a) CONTROL, a pick of the first question, and no `ask` at all, give today's order; (b) a pick of the second gives the same candidates (none formed, none
    dropped), those whose `occasion` is that question first and the rest after in today's order, and the sheet carries the question picked. `moved` is asserted, so a
    season in which the pick reordered nothing is a red test and not a vacuous one."""
    from ..decision.sheet import development_space, situation
    checked, moved = [0], [0]

    def per_person(p, v, ranked, terms):
        if len(v.questions) < 2 or checked[0] >= 40:
            return
        fx, verbs, draw = _CHOOSER["fx"], _CHOOSER["verbs"], _CHOOSER["draw"]
        mint = lambda who, verb, subj: f"{who}:{verb}:{subj}"

        def sheet_under(ask):
            got: list = []
            development_space(fx, mint, lambda sheet: (got.append(sheet), [])[1], verbs, draw, ask=ask)(p, v, None, lambda: 5)
            return got[0]

        def order(sheet):
            return [(c.verb, c.subject) for c in sheet.candidates]
        plain, first, second = sheet_under(None), sheet_under(lambda s: 0), sheet_under(lambda s: 1)
        assert order(first) == order(plain) == [(c.verb, c.subject) for c in ranked], p.id
        assert first.question is plain.question and plain.question is v.question
        rows = _offer(p, v).rows
        want = v.questions[1].id
        expected = [(r.candidate.verb, r.candidate.subject) for r in rows if r.occasion == want] \
            + [(r.candidate.verb, r.candidate.subject) for r in rows if r.occasion != want]
        assert order(second) == expected, (p.id, want)
        assert second.question.id == want
        shown = situation(p, v, lambda: 5).asked
        assert [a.question.id for a in shown] == [q.id for q in v.questions]
        checked[0] += 1
        moved[0] += order(second) != order(plain)

    def aggregate_all(w):
        w.fixtures = w.fixtures.sweep("question_aggregation_rule", "all")
    _deliberations(0, per_person, overlay=aggregate_all)
    assert checked[0] == 40, f"only {checked[0]} deliberations asked two questions: the arm did not run"
    assert moved[0] >= 1, "a pick of the second question reordered no deliberation: the arm observed nothing"


# -- gate 3 of `11_GO_fidelity_and_campaign_modes` (B34.08) ------------------------------------------------------

@pytest.mark.slow
def test_scene_budget_overlay_gives_three_scenes():
    """FIDELITY GATE 3 (B34.08): difficulty is a `Fixtures` overlay chosen at world build, and nothing else in the engine reads one. A realm built with `scene_budget`
    swept to 3 (`on_build`, before the seat is bound) is played one season with `p_npc_001` seated on the shipped ranking. (a) The overlay differs from the shipped
    `Fixtures` in that one key. (b) His own `budget` at his first deliberation is 3, the shipped 5's replacement, and he spends no more than three scene actions in
    the season (the sum of `Scene.cost` over the scenes the fold stored with him as actor), at least one. (c) The season's `content_hash` is not the plain run's,
    which is the control: the same seed and the same chooser, with the shipped fixtures, are `test_transcript_hash_equals_plain_run`'s hash."""
    from ..data.fixtures import DEFAULT_FIXTURES
    from ..decision.sheet import take_ranked
    from ..harness import scenarios as SC
    shipped = DEFAULT_FIXTURES.get("scene_budget")
    assert shipped == 5
    budgets: list = []
    built: list = []

    def pick(sheet):
        budgets.append(sheet.budget)
        return take_ranked(sheet)

    def overlay(w):
        built.append(w.fixtures)
        w.fixtures = w.fixtures.sweep("scene_budget", 3)
    r = SC.run("life", 0, 1, pick=pick, person=SEATED, on_build=overlay)
    w = r["world"]
    changed = {k for k in built[0]._v if built[0]._v[k] != w.fixtures._v[k]}
    assert changed == {"scene_budget"}, changed
    assert budgets and budgets[0] == 3, budgets
    ext = w.fixtures.get("extended_scene_cost")
    spent = sum(sc.cost(ext) for sc in w.acts.scenes() if sc.actor == SEATED)
    assert 1 <= spent <= 3, spent
    plain = build_realm(0)
    POP.run(1, 0, w=plain)
    assert r["hash"] != plain.content_hash(), "scene_budget swept to 3 left the season's hash where the shipped fixtures put it"


# -- B34.19: the transcript stops (`U5a_CORE_owed_edits` §F) ----------------------------------------------------------------------------------------
# GAME-STATE, lane season_loop. The ending is planted through `world_q.endings_reached` (a roster ending reached once a season has been played, an
# `EndingReached` of its own id); the seats are persons of the built realm read by `world_q.continuations`, never named.

def _planted_ending(monkeypatch):
    from ..queries import world_q
    monkeypatch.setattr(world_q, "endings_reached",
                        lambda w: [world_q.EndingReached("planted_end", True, (), (), ())] if w.tick > 0 else [])


def _seats():
    """A person of the realm with no continuation and one with (the realm as `life` builds it), read by the Query."""
    from ..queries import world_q
    w = build_realm(0)
    by = {p: len(world_q.continuations(w, w.persons[p])) for p in sorted(w.persons)}
    return next(p for p, n in by.items() if n == 0), next(p for p, n in by.items() if n >= 1)


def test_a_reached_ending_with_no_continuation_stops_the_transcript(monkeypatch):
    """§F rule 1, no continuation: a roster ending reached in season 1 and a seat with no continuation ends the transcript at season 1, naming the ending's id,
    though two seasons were asked. The control is the run with nothing planted, which plays both."""
    from ..harness import play_surface as PS
    alone, _ = _seats()
    plain = PS.transcript("life", 0, 2, alone, out=lambda s: None)
    assert (plain["seasons"], plain["ending"]) == (2, "unfinished"), plain["ending"]
    _planted_ending(monkeypatch)
    lines: list = []
    r = PS.transcript("life", 0, 2, alone, out=lines.append)
    assert (r["seasons"], r["ending"], r["kind"]) == (1, "realm_fallen", "lost")     # the planted ending's holders are nobody's: no commit of his is to them
    assert any("planted_end" in line for line in lines), lines[-6:]
    assert lines[-1] == "ENDING realm_fallen lost", lines[-1]


def test_an_ending_with_a_continuation_plays_on(monkeypatch):
    """§F rule 1, with a continuation: the same planted ending and a seat who has one. The transcript records the ending and plays both seasons."""
    from ..harness import play_surface as PS
    _, heir = _seats()
    _planted_ending(monkeypatch)
    lines: list = []
    r = PS.transcript("life", 0, 2, heir, out=lines.append)
    assert (r["seasons"], r["ending"]) == (2, "unfinished"), (r["seasons"], r["ending"])
    assert r["recorded"] == ["planted_end"] and any("planted_end" in line for line in lines)


def test_a_killed_seat_continues_under_the_heir(monkeypatch):
    """§F rule 2: the seat dies (planted through the row's `ending`, as the matter step would kill him) and `carry_on` offers his living ties. The transcript says it
    re-seated him and the second season is deliberated by the one he became."""
    from ..data.matrix import Step, WriteClass
    from ..harness import play_surface as PS, scenarios as SC
    from ..loop.matter import _die
    from ..loop.driver import mint_token
    from ..queries import world_q
    _, pid = _seats()
    heir = world_q.continuations(build_realm(0), build_realm(0).persons[pid])[0].person
    row, done = SC.SCENARIOS["life"], []

    def ending(w, who, left):
        if not done:
            done.append(who)
            w.step, w._emitted_by_write = Step.MATTER, []
            _die(w, mint_token(w, WriteClass.MATTER), who)
        return row.ending(w, who, left)
    monkeypatch.setitem(SC.SCENARIOS, "life_dying", SC.Scenario(build=build_realm, seat=None, ending=ending, kinds=row.kinds))
    lines: list = []
    r = PS.transcript("life_dying", 0, 2, pid, out=lines.append)
    assert done == [pid] and pid not in r["world"].persons
    assert r["passed"] == (pid, heir) and r["seat"] == heir and r["seasons"] == 2, (r["passed"], r["seasons"])
    assert any(line.startswith("-- re-seated") and pid in line and heir in line for line in lines), lines[-8:]
    assert any(line.startswith("-- deliberation") and line.endswith(heir) for line in lines)


# -- B34.20: a run's ending reaches the surface, with its kind (`IS-B3-GO-02`) ------------------------------------------------------------------------
# GAME-STATE, lane season_loop. (1) one season of the realm through the transcript on a planted reader; (2) the hand-built governance world `test_in27_endings.py`
# plants its `crowned_reeve` row on, no season played; (3) the readers on the built realm, no season played.

def test_the_transcript_stops_on_an_ending_and_prints_its_kind(monkeypatch):
    """A planted reader names `planted_won` once a season has been played, of a row whose `kinds` makes it `won`; three seasons are asked. The transcript stops at one,
    prints the seated person's chronicle and his WHOLE `account` (one row a claim of his ledger), and its last line is `ENDING planted_won won`, once."""
    from ..decision.sheet import account
    from ..harness import play_surface as PS, scenarios as SC
    monkeypatch.setitem(SC.SCENARIOS, "planted", SC.Scenario(build=build_realm, seat=None, kinds={"planted_won": "won"},
                                                             ending=lambda w, pid, left: "planted_won" if w.tick > 0 else None))
    lines: list = []
    held_sizes: list = []                                  # his ledger's size at each deliberation, read where the printer is called
    real = PS.deliberation_lines
    monkeypatch.setattr(PS, "deliberation_lines", lambda w, sheet, verbs=None: (held_sizes.append(len(w.persons[sheet.person_id].ledger)), real(w, sheet, verbs))[1])
    r = PS.transcript("planted", 0, 3, SEATED, out=lines.append)
    assert (r["seasons"], r["ending"], r["kind"]) == (1, "planted_won", "won"), (r["seasons"], r["ending"], r["kind"])
    assert [x for x in lines if x.startswith("ENDING")] == ["ENDING planted_won won"] and lines[-1] == "ENDING planted_won won", lines[-4:]
    assert lines.index(f"content_hash {r['hash']}") < len(lines) - 1
    held = r["world"].persons[SEATED]
    start = next(i for i, x in enumerate(lines) if x.startswith("-- the ending"))
    whole = [x for x in lines[start:] if x.startswith("   learned ")]
    assert len(whole) == len(account(held, ())) == len(held.ledger) >= 1, (len(whole), len(held.ledger))
    assert SEATED in lines[start] and f"{len(held.ledger)} claim" in lines[start], lines[start]
    # what he learned between his first and second deliberations at tick 0 is not dropped for sharing the stamp of the lap just played (his ledger gained claims there)
    learned = [int(x.split()[3]) for x in lines if x.startswith("   he has learned ")]
    assert learned and learned[0] >= 1 and learned[:len(held_sizes) - 1] == [b - a for a, b in zip(held_sizes, held_sizes[1:])], (learned, held_sizes)


def _reeve_world(monkeypatch):
    """The governance world with `crowned_reeve` planted (`test_in27_endings.REEVE_ROW`, here a VICTORY row: only one names a holding side): `p_king` confers `off_reeve` on `p_mid`, a Crown man, and the row is reached.
    Returns `(w, reached)`; three more persons stand for the three seats: `p_other` committed to the Crown, `p_high` to the Church, `p_low` to nobody."""
    from ..queries import world_q as Q
    from ..state.carriers import Tenure
    from .test_g3_not_yours import _gov_world
    from .test_in27_endings import CHURCH, CROWN, REEVE_ROW, _fold
    w, d = _gov_world()
    monkeypatch.setattr(Q, "ENDINGS", {"crowned_reeve": dataclasses.replace(REEVE_ROW["crowned_reeve"], victory=True)})
    w.add_tenure(Tenure("t_mid_crown", "p_mid", CROWN, "commit", 0))
    w.add_tenure(Tenure("t_other_crown", "p_other", CROWN, "commit", 0))
    w.add_tenure(Tenure("t_high_church", "p_high", CHURCH, "commit", 0))
    assert _fold(w, d, Act(id="in27_cf", actor="p_king", verb="confer", via="off_crown",
                           payload={"subject": "off_reeve", "office": "off_reeve", "to": "p_mid"})) == ["tenure.opened"]
    return w, Q.endings_reached(w)


def test_a_realm_ending_is_held_for_a_seat_of_the_holding_faction_and_fallen_for_another(monkeypatch):
    """`crowned_reeve` (a victory row here) is reached with a Crown man on the Reeve's seat. A seat with a live `commit` to the Crown reads `realm_held` (`won`); a seat committed to the
    Church reads `realm_fallen`, and so does one committed to nobody (`lost`); nobody seated stays `realm_ended` (`drawn`; the life row reads `line_extinct` first). Each seat has no continuation (the
    transcript's own stop test), so the reader names an ending at all; CONTROL: nothing reached names none, whoever sits."""
    from ..harness import play_surface as PS, scenarios as SC
    from ..queries import world_q as Q
    w, reached = _reeve_world(monkeypatch)
    assert [(e.ending, e.victory) for e in reached] == [("crowned_reeve", True)] and len(reached[0].holds) == 1, reached
    monkeypatch.setattr(Q, "endings_reached", lambda world: reached)
    seats = {"p_other": ("realm_held", "won"), "p_high": ("realm_fallen", "lost"), "p_low": ("realm_fallen", "lost"), None: ("realm_ended", "drawn")}
    for pid, (name, kind) in seats.items():
        assert not PS.has_continuation(w, pid), f"fixture: {pid} has a continuation, so no ending is read"
        for row in ("season", "life"):
            got = SC.SCENARIOS[row].ending(w, pid, 1)
            if row == "life" and pid is None:       # the life row reads his line first (`life_ending`'s own order)
                name, kind = "line_extinct", "lost"
            assert got == name and SC.SCENARIOS[row].kinds[got] == kind, (row, pid, got)
    # A REACHED ROW THAT IS NOT A VICTORY names no holding side (the shipped `theocracy` is `victory: false`): every seat reads `realm_ended`, whichever faction it is committed to.
    monkeypatch.setattr(Q, "endings_reached", lambda world: [dataclasses.replace(reached[0], victory=False)])
    for pid in ("p_other", "p_high", "p_low"):
        for row in ("season", "life"):
            got = SC.SCENARIOS[row].ending(w, pid, 1)
            assert got == "realm_ended" and SC.SCENARIOS[row].kinds[got] == "drawn", (row, pid, got)
    monkeypatch.setattr(Q, "endings_reached", lambda world: [])
    assert SC.season_ending(w, "p_other", 1) is None and SC.life_ending(w, "p_other", 1) is None


def test_line_extinct_is_lost_and_a_living_continuation_is_not_an_ending(monkeypatch):
    """On the built realm: with nothing reached and nobody seated the season row names `line_extinct`, `lost`. With an ending reached, a seat that has a living
    continuation is no ending (the run plays on), and the same ending is one for a seat that has none."""
    from ..harness import scenarios as SC
    from ..queries import world_q as Q
    w = build_realm(0)
    by = {p: len(Q.continuations(w, w.persons[p])) for p in sorted(w.persons)}
    alone, heir = next(p for p, n in by.items() if n == 0), next(p for p, n in by.items() if n >= 1)
    assert SC.season_ending(w, None, 3) == "line_extinct" and SC.SCENARIOS["season"].kinds["line_extinct"] == "lost"
    assert SC.life_ending(w, None, 3) == "line_extinct" and SC.SCENARIOS["life"].kinds["line_extinct"] == "lost"
    monkeypatch.setattr(Q, "endings_reached", lambda world: [Q.EndingReached("planted_end", True, (), (), ())])
    assert SC.season_ending(w, heir, 3) is None and SC.life_ending(w, heir, 3) not in ("realm_ended", "realm_held", "realm_fallen")
    assert SC.season_ending(w, alone, 3) == "realm_fallen" and SC.life_ending(w, alone, 3) == "realm_fallen"
