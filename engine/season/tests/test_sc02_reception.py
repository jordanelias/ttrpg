"""v9 SC-02 `22a`, piece 1 -- proceedings PHASE 3 steps 17, 18 and 20 (`19_PLAN.md`, intent only):
`reception` (the room's reading of the speaker, resolver-side), `proofs` (weighed by remove, discounted
by the mirror) and route erosion (the single called bluff, inside reception). B24.02 (F8, option B): neither Query reads
a ledger but the ACTOR'S OWN; what the rest of the bench and the opponent have said in public is read off their live `commit` edges.

WHAT IS BUILT, asked of the real host builder (`seam/wrappers/sigma.py`), the real module
(`modules/social_contest/roll.py::obstacle`) and the real fold on a HAND-BUILT world (`probes.tiny_world`
through `test_u7_remit._world`: `p_high` holds `off_duke`, whose bench sits over `Hh`; the speaker `p_low`
and his party `p_mid` live in `Hh`; `p_other` lives there and sits on no bench):
  * `world_q.reception(w, target, audience, actor)` -- the own term: the actor's own deed claims about the target when he sits in the
    audience (`remove_weight(source)` x decayed confidence x his valence, arm 1, the alignment table; arm 2 was never authored and the sweep
    is open, `hole_register.yaml` H-215), plus the commit term: each other member's live HOLDS commits to a Proposition about the target,
    each at `deed_valence` alone; summed; `reception_gain` scales it: its hostile half into the obstacle (the `reception` member), its
    favourable half into `favour` levels (`H-215`, B05.17);
  * `world_q.proofs(w, actor, opponent, audience)` -- the actor's deed claims about the opponent weighed by
    remove, zero for any the opponent mirrors (a live commit of his to a Proposition of the same subject and predicate); `proof_level`
    (`H-216`, B05.17: a proof is a named level of leverage, never an obstacle reduction);
  * route erosion -- `rosters.yaml: standing_routes`: an ACTOR who saw a dominance-route deed done TO the
    target zeroes every dominance-route deed of his no newer than it (the own term only).

THE FALSIFIERS (`19_PLAN.md` :537, :550, :578), each an assertion below that observes its failure:
  * step 17: a bench's obstacle invariant under a change to a member's commits; the Query reachable from a
    decision -- `test_sc02_17_...`; B24.02: no other judge's LEDGER moves it (`test_sc02_world_a_*`);
  * step 18: the mirrored proof moves the obstacle -- `test_sc02_18_...`;
  * step 20: a called bluff leaves the weight unchanged -- `test_sc02_20_...`.
"""

from __future__ import annotations

import ast
import math
import random
from engine.dice_engine import draw
from pathlib import Path

from dataclasses import replace

from engine.dice_engine.sigma_leverage import LEVEL_SIGMA, band_odds, levels_to_net_sigma, net_boost

from ..data import files
from ..data.fixtures import DEFAULT_FIXTURES
from ..data.rosters import DOMINANCE_KINDS, REMOVE_ORDINAL, SEEN_PREDICATE
from ..data import verbs as _verbs
from ..epistemic import Seen
from ..queries import person_q, world_q
from ..seam import ladder
from ..seam.wrappers import sigma
from ..state.carriers import Claim, Office, Proposition, Tenure
from .test_sc01_obstacle_ceiling import _module
from .test_u7_remit import _world

SPEAKER, PARTY, HEARER, NOBODY = "p_low", "p_mid", "p_high", "p_other"
PRIZE = "a matter"
VERB = "arrest"         # B24.10: the single roll's own verb the bench-hearing is exercised through (`speak` and, since B24.08, `determine` proceed; was `determine`)
SEASON_DIR = Path(__file__).resolve().parents[1]

# The pursuit the hearer is given: the tiny world's persons hold none, so every valence reads 0 and
# reception would be zero BY CONSTRUCTION -- a fake control. One pursuit makes the hearer judge.
PURSUIT = "honour"


def _claim(cid, holder, subject, kind, *, source="firsthand", chain=(), when=0, rnd=0, conf=100):
    return Claim(cid, holder, subject, kind, True, when, source, conf, "own", rnd, chain=chain)


def _seen(cid, holder, subject, who, *, when=0, rnd=0):
    stratum = _verbs.VERB_TABLE["fight"].stratum
    return Claim(cid, holder, subject, SEEN_PREDICATE, Seen(stratum=stratum, marks=(), who=who),
                 when, "firsthand", 100, "own", rnd)


def _judging_world(**fixtures):
    w, d = _world(**fixtures)
    w.persons[HEARER].pursuits = {PURSUIT: 1.0}
    assert world_q.judging_set(w, world_q.place_of(w, SPEAKER)) == [HEARER]
    return w, d


def _lean(w, kind):
    axis_w = person_q.projected_axes(w.persons[HEARER])
    return person_q.deed_valence(axis_w, _claim("probe", HEARER, SPEAKER, kind))


def _kind_with_lean(w, sign=+1, among=None):
    """The unpaired deed kind the hearer leans on hardest in `sign`'s direction (ties by name)."""
    kinds = sorted((among or _verbs.DEED_KINDS) - person_q.PAIRED_KINDS)
    best = max(kinds, key=lambda k: (sign * _lean(w, k), k))
    assert sign * _lean(w, best) > 0, f"no kind leans {sign:+d} for {PURSUIT!r}: the fixture is inert"
    return best


_PROP = [0]


def _commit(w, judge, subject, kind, *, value=True, mood="HOLDS", live=True):
    """`judge` publicly commits (a live `commit` edge, `_eff_commit`'s shape) to a Proposition that `subject` did `kind`: the room's route."""
    _PROP[0] += 1
    pid = f"prop_{_PROP[0]}"
    w.propositions[pid] = Proposition(pid, mood, subject, kind, value, 0)
    w.add_tenure(Tenure(f"t_{pid}", judge, pid, "commit", 0, None if live else 1))
    return w.propositions[pid]


def _kinds_leaning(w, sign, n=None):
    """The unpaired deed kinds the hearer leans on in `sign`'s direction, strongest first (`n` of them, or all)."""
    kinds = sorted(_verbs.DEED_KINDS - person_q.PAIRED_KINDS)
    ranked = sorted((k for k in kinds if sign * _lean(w, k) > 0), key=lambda k: (-sign * _lean(w, k), k))
    return ranked if n is None else ranked[:n]


def _hearer_commits(w, sign, n):
    """The bench's commit term, `n` distinct kinds (a judge's commits to one kind count once): the hearer's HOLDS commits about the speaker."""
    kinds = _kinds_leaning(w, sign, n)
    assert len(kinds) == n, f"only {len(kinds)} kinds lean {sign:+d}"
    for k in kinds:
        _commit(w, HEARER, SPEAKER, k)
    return kinds


def _hearer_commits_to(w, sign, total):
    """Commits, strongest kind first, until the hearer's commit term reaches at least `total` (and under `total + 1`)."""
    got = 0.0
    for k in _kinds_leaning(w, sign):
        if got >= total:
            break
        _commit(w, HEARER, SPEAKER, k)
        got += abs(_lean(w, k))
    assert total <= got < total + 1.0, (total, got)
    return got


def _rec(w, target=SPEAKER, actor=HEARER):
    """`reception` of `target` by the bench over `Hh`, asked as `actor` acts. The default is the HEARER, the one whose own ledger it may read (the
    own term); `actor=SPEAKER` is a `speak` or `determine` by the target, where only the bench's commits are read."""
    return world_q.reception(w, target, world_q.judging_set(w, "Hh"), actor)


def _ob(w, actor=SPEAKER, subject=PARTY):
    """The composed obstacle of one draw of a roll whose prize a bench hears, through the real adapter and module entry. B24p.99: the verb
    that lends the pool is `determine` (still on the single roll; `speak` proceeds and is never pooled here), the prize row `a matter`'s
    own `heard_by: bench` is what the seam reads."""
    out = sigma.resolve(w, [actor, subject], ["root"], PRIZE, verb=VERB, subject=subject,
                        rng=draw.seeded(draw.H2("test_sc02_reception", 0)), rung=world_q.place_of(w, actor))
    assert out["status"] == "RESOLVED", out
    return out["ob"]


def _input(w, actor=SPEAKER, subject=PARTY):
    return sigma.contest_input(w, [actor, subject], verb=VERB, subject=subject,
                               room=world_q.place_of(w, actor))


# ================================================================================================
# STEP 17 -- RECEPTION
# ================================================================================================

def test_sc02_17_two_benches_differing_only_in_one_commit_band_differently_for_the_same_draw():
    """`19_PLAN.md` step 17's artifact: identical seats and convictions, one member's public commits differ, and
    the same seeded roll (a bench-heard prize) resolves at different bands. FALSIFIER: the obstacle invariant under the
    commit change (asserted on every draw, and on the band over the sweep)."""
    plain, d_plain = _judging_world()
    heard, d_heard = _judging_world()
    _hearer_commits_to(heard, +1, 2.0)                  # enough favour to reach the Ob floor from 2
    assert _rec(plain, actor=SPEAKER) == 0.0
    assert _rec(heard, actor=SPEAKER) > 0.0
    # B05.17: the favourable bench is LEVERAGE (`favour`), not a lower obstacle: what the speaker brings rises, what stands against him does not.
    assert _input(heard).leverage > _input(plain).leverage, (_input(heard).leverage, _input(plain).leverage)
    assert _ob(heard) == _ob(plain), (_ob(heard), _ob(plain))
    differ = checked = 0
    for i in range(40):                       # B24p.99: the same seeded roll through the seam, graded on the one ladder (`speak` proceeds)
        a, b = (sigma.resolve(w, [SPEAKER, PARTY], ["root"], PRIZE, verb=VERB, subject=PARTY,
                              rng=draw.seeded(draw.H2("test_sc02_reception_band", i)), rung="Hh") for w in (plain, heard))
        assert a["status"] == b["status"] == "RESOLVED", (a, b)
        differ += ladder.degree_of(a) != ladder.degree_of(b)
        checked += 1
    assert checked == 40
    assert differ >= 1, "no draw banded differently: the bench's ledger did not reach the outcome"


def test_sc02_17_a_commit_off_the_bench_moves_nothing():
    """THE CONTROL: the same commits by a person who sits on no bench over `Hh` leave reception at 0 and
    the obstacle at its base, so what moved it above is the BENCH's commits, not any commit."""
    w, _d = _judging_world()
    w.persons[NOBODY].pursuits = {PURSUIT: 1.0}
    base = _ob(w)
    for kind in _kinds_leaning(w, +1, 5):
        _commit(w, NOBODY, SPEAKER, kind)
    assert _rec(w, actor=SPEAKER) == 0.0
    assert _ob(w) == base


def test_sc02_17_a_told_claim_counts_strictly_less_in_the_own_term_than_the_same_claim_firsthand():
    """Step 17's second artifact, over the ordinal of remove: firsthand > knot-sourced > told > inferred,
    each strictly, and every rank still counts. B24.02: the claim is the ACTOR'S OWN (the own term, the one route a ledger reaches
    `reception` by), so the actor is the hearer and the target the speaker."""
    got = {}
    for source in REMOVE_ORDINAL:
        w, _d = _judging_world()
        kind = _kind_with_lean(w, +1)
        chain = ("p_king",) if source == "told_by" else ()
        w.persons[HEARER].ledger.append(_claim("c", HEARER, SPEAKER, kind, source=source, chain=chain))
        got[source] = _rec(w)
    ranked = [got[s] for s in REMOVE_ORDINAL]
    assert ranked == sorted(ranked, reverse=True) and len(set(ranked)) == len(ranked), got
    assert got["firsthand"] > got["told_by"] > 0.0, got
    assert min(ranked) > 0.0, got                                            # even the most removed rank counts


def test_sc02_17_decayed_confidence_counts_less_and_a_hostile_bench_reads_negative():
    w, _d = _judging_world()
    kind = _kind_with_lean(w, +1)
    w.persons[HEARER].ledger.append(_claim("full", HEARER, SPEAKER, kind))
    full = _rec(w)
    w.persons[HEARER].ledger[-1] = _claim("half", HEARER, SPEAKER, kind, conf=50)
    assert _rec(w) == full / 2                                               # the own term: a decayed claim of the actor's own
    hostile = _kind_with_lean(w, -1)
    w.persons[HEARER].ledger[-1] = _claim("bad", HEARER, SPEAKER, hostile)
    assert _rec(w) < 0.0
    w, _d = _judging_world()                                                # and the same hostile reading, as the bench's commit
    _commit(w, HEARER, SPEAKER, hostile)
    assert _rec(w, actor=SPEAKER) == _lean(w, hostile) < 0.0
    # Under the FIXED ceiling (`H-213`, 2) a hostile room cannot raise the
    # obstacle; one notch up it does; and under the shipped per-pool arm (CP-T01-06) it raises it up to
    # the pool's cap (pool 2: 2.842). Stated in `roll.obstacle`'s docstring and in H-215.
    from dataclasses import replace
    inp = _input(w)
    assert inp.ceiling_per_pool is True
    obstacle = lambda record: _module().obstacle(record)[0]          # B05.14: the composer returns `(ob, terms)`
    fixed = replace(inp, ceiling_per_pool=False)
    assert obstacle(fixed) == inp.obstacle_ceiling
    assert obstacle(replace(fixed, obstacle_ceiling=3.0)) > 2.0
    assert 2.0 < obstacle(inp) <= 2.0 * inp.pool


def test_sc02_17_reception_and_proofs_take_the_world_first():
    """The AST half of step 17's artifact: both Queries take `w: World` first, which is what puts them
    under the AX-2 scan (`test_season_shape.py::test_decision_package_never_names_world_anywhere_under_it`
    forbids `decision/` any `queries.*` but `person_q` and any imported name whose signature takes a
    `World`; this file does not re-walk `decision/`). FALSIFIER: a Query whose first parameter is not the
    world would leave that scan's second half blind."""
    tree = ast.parse((SEASON_DIR / "queries" / "world_q.py").read_text())
    found = {}
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in ("reception", "proofs"):
            first = node.args.args[0]
            found[node.name] = (first.arg, ast.unparse(first.annotation) if first.annotation else None,
                                [a.arg for a in node.args.args])
    # B24.02: the ACTOR is a parameter of both, so a call passing any other person reads as a defect at the site
    assert found == {"reception": ("w", "World", ["w", "target", "audience", "actor"]),
                     "proofs": ("w", "World", ["w", "actor", "opponent", "audience", "admitted"])}, found


def test_sc02_17_only_a_prize_a_room_hears_reads_the_room(monkeypatch):
    """`heard_by: bench` is on `a matter` alone: an `arrest` (`a standing`) or an inquiry by the same actor
    at the same rung carries the record's no-room defaults, so every other social roll is as it was."""
    w, _d = _judging_world()
    _commit(w, HEARER, SPEAKER, _kind_with_lean(w, +1))
    seen = {}
    real = sigma._read_social_roll

    def spy(*a, **kw):
        built = real(*a, **kw)
        seen[kw.get("verb")] = built[0]
        return built
    monkeypatch.setattr(sigma, "_read_social_roll", spy)
    for prize, verb in ((PRIZE, "issue"), ("a standing", "arrest")):       # B24.10: both still on the single roll (`speak`, `tell`, `determine` proceed; was `determine`)
        sigma.resolve(w, [SPEAKER, PARTY], ["root"], prize, verb=verb, subject=PARTY,
                      rng=draw.seeded(draw.H2("test_sc02_reception", 0)), rung="Hh")
    assert seen["issue"].reception > 0.0
    assert seen["arrest"].reception == 0.0 and seen["arrest"].reception_gain == 0.0, seen["arrest"]


def test_sc02_17_a_misspelled_room_refuses_at_boot_naming_the_row(monkeypatch):
    """`heard_by:` names a room the host reads (`manifest/registry.py::HEARD_BY_ROOMS`) or the boot check
    refuses, naming the row; the shipped rows are the control."""
    from ..data.rosters import roster_map
    from ..gaps import Unspecified
    from ..manifest import registry
    import pytest
    assert registry.check_rows()                         # the control: the shipped rows pass
    row = roster_map("contest_subsystems", "prizes")[PRIZE]
    assert row["heard_by"] == "bench"
    monkeypatch.setitem(row, "heard_by", "benchh")
    with pytest.raises(Unspecified, match=r"contest:'a matter' declares `heard_by: 'benchh'`"):
        registry.check_rows()


# ================================================================================================
# STEP 18 -- PROOFS, BY REMOVE AND THE MIRROR
# ================================================================================================

def test_sc02_18_a_mirrored_proof_moves_the_obstacle_by_exactly_zero_and_an_unmirrored_one_by_step_x_remove():
    """`19_PLAN.md` step 18's artifact, re-pointed at B05.17: a proof is LEVERAGE (`proofs`: one `proof_level` per whole unit of
    `world_q.proofs`), so what it moves is `leverage`, and it moves the obstacle by exactly nothing. The speaker holds four deed
    claims about his opponent at each remove (a unit is whole, so one claim at the lowest rank would round to none); the hearer
    holds nothing, so reception is 0 and only the proofs source moves the leverage. B24.02: the opponent mirrors a proof by a live COMMIT of his
    to a Proposition of the proof's subject and predicate (his ledger mirrors nothing).
    FALSIFIER: the mirrored proof moves the leverage (exact equality with the base, no tolerance), or an unmirrored one moves the obstacle."""
    kind = sorted(_verbs.DEED_KINDS - person_q.PAIRED_KINDS)[0]
    checked = 0
    for source in REMOVE_ORDINAL:
        chain = ("p_king",) if source == "told_by" else ()
        w, _d = _judging_world()
        base, base_ob = _input(w).leverage, _ob(w)
        level = w.fixtures.get("proof_level")
        assert level is not None and base == 0.0, "the shipped level is the control: the falsifier could not see a move"
        for i in range(4):
            w.persons[SPEAKER].ledger.append(_claim(f"pf{i}", SPEAKER, PARTY, kind, source=source, chain=chain))
        assert _rec(w, actor=SPEAKER) == 0.0
        owed = levels_to_net_sigma([level] * int(4 * world_q.remove_weight(source) + 0.5))
        assert owed > 0.0 and _input(w).leverage == base + owed, (source, _input(w).leverage, owed)
        assert _ob(w) == base_ob, (source, _ob(w), base_ob)                 # the obstacle is not where a proof acts
        # NEAR-MISSES DO NOT MIRROR: the same predicate about another subject, and the same subject
        # under another predicate, leave the proof standing (the mirror keys on BOTH); nor does his LEDGER, nor a commit he has ended.
        other_kind = next(k for k in sorted(_verbs.DEED_KINDS - person_q.PAIRED_KINDS) if k != kind)
        _commit(w, PARTY, NOBODY, kind)
        _commit(w, PARTY, PARTY, other_kind)
        _commit(w, PARTY, PARTY, kind, live=False)
        w.persons[PARTY].ledger.append(_claim("his_own_deed", PARTY, PARTY, kind))
        assert _input(w).leverage == base + owed, "a near-miss mirrored a proof"
        # THE MIRROR: the opponent has committed, live, to a Proposition of the same subject and predicate (any value: a denial answers the
        # proof on the record) -> exactly zero.
        _commit(w, PARTY, PARTY, kind, value=False)
        assert world_q.proofs(w, SPEAKER, PARTY, world_q.judging_set(w, "Hh")) == 0.0
        assert _input(w).leverage == base, (source, _input(w).leverage, base)
        assert _ob(w) == base_ob, (source, _ob(w), base_ob)
        checked += 1
    assert checked == len(REMOVE_ORDINAL)


def test_sc02_18_proofs_never_move_the_obstacle_and_a_non_person_mirrors_nothing():
    """B05.17: forty proofs lower no obstacle (it was floored at `OB_MIN` before; nothing lowers it now, P-232 by construction) and
    raise the leverage; the leverage the soft cap bounds is the bound (`net_boost`)."""
    w0, _d0 = _judging_world()
    base_ob, base_lev = _ob(w0), _input(w0).leverage
    w, _d = _judging_world()
    kind = sorted(_verbs.DEED_KINDS - person_q.PAIRED_KINDS)[0]
    for i in range(40):
        w.persons[SPEAKER].ledger.append(_claim(f"pf{i}", SPEAKER, PARTY, kind))
    assert _ob(w) == base_ob and _input(w).leverage > base_lev           # the obstacle unmoved, the leverage up
    assert net_boost(_input(w).leverage, 4) < 1.5 * 0.8 * 2.0 + 1e-9     # bounded: the soft cap's M_MAX, at pool 4
    assert world_q.proofs(w, SPEAKER, None, world_q.judging_set(w, "Hh")) == 0.0
    # A NON-PERSON OPPONENT holds no ledger, so nothing of his mirrors a proof: a deed claim the speaker
    # holds about the rung `Hh` itself is counted whole (observable: it is not zero).
    w2, _d2 = _judging_world()
    assert "Hh" not in w2.persons
    w2.persons[SPEAKER].ledger.append(_claim("pr", SPEAKER, "Hh", kind))
    assert world_q.proofs(w2, SPEAKER, "Hh", world_q.judging_set(w2, "Hh")) == world_q.remove_weight("firsthand") > 0.0


def test_sc02_18_proofs_are_spent_on_a_bench_and_never_on_an_empty_room():
    """With nobody on the bench there is no one to spend a proof on (`reception`'s own rule): the same
    held proof counts on `Hh` and counts zero with no venue (a placeless speaker) -- the control."""
    w, _d = _judging_world()
    kind = sorted(_verbs.DEED_KINDS - person_q.PAIRED_KINDS)[0]
    w.persons[SPEAKER].ledger.append(_claim("pf", SPEAKER, PARTY, kind))
    assert world_q.proofs(w, SPEAKER, PARTY, world_q.judging_set(w, "Hh")) == world_q.remove_weight("firsthand") > 0.0
    assert world_q.proofs(w, SPEAKER, PARTY, ()) == 0.0
    assert world_q.judging_set(w, "Hh") == [HEARER]
    # the only seated person IS the speaker: nobody else is in the room
    w.persons[HEARER].ledger.append(_claim("pf2", HEARER, PARTY, kind))
    assert world_q.proofs(w, HEARER, PARTY, world_q.judging_set(w, "Hh")) == 0.0


def test_sc02_17_a_man_does_not_receive_himself():
    """The speaker is excluded from his own bench: a seated person's reception of HIMSELF is 0 though his
    ledger holds deed claims of his own that lean (CONTROL: the same claims read non-zero when the
    speaker is someone else and the holder is on the bench)."""
    w, _d = _judging_world()
    kind = _kind_with_lean(w, +1)
    w.persons[HEARER].ledger.append(_claim("mine", HEARER, HEARER, kind))
    assert _rec(w, HEARER) == 0.0
    w.persons[HEARER].ledger.append(_claim("his", HEARER, SPEAKER, kind))
    assert _rec(w, SPEAKER) != 0.0


# ================================================================================================
# STEP 20 -- ROUTE EROSION: THE SINGLE CALLED BLUFF
# ================================================================================================

def _feared_lord(w):
    """The speaker governs by fear in the hearer's eyes: dominance-route deeds the hearer saw (tick 0)."""
    kind = _kind_with_lean(w, +1, among=DOMINANCE_KINDS) if any(
        _lean(w, k) > 0 for k in DOMINANCE_KINDS - person_q.PAIRED_KINDS) else sorted(
        DOMINANCE_KINDS - person_q.PAIRED_KINDS)[0]
    assert _lean(w, kind) != 0.0, kind
    for i in range(3):
        w.persons[HEARER].ledger.append(_claim(f"dom{i}", HEARER, SPEAKER, kind, when=0))
    return kind


def test_sc02_20_the_nobodys_one_success_collapses_the_lord_and_his_failure_leaves_him_intact():
    """`19_PLAN.md` step 20's artifact. The lord (`p_low`) is challenged by a nobody (`p_other`) at tick 1.
      * SUCCESS: the hearer saw the nobody wound the lord -- `(p_low, body.changed)` paired by a sighting
        whose `who` is the nobody. Every dominance deed of the lord's no newer than it counts zero.
      * FAILURE: the hearer saw the lord wound the nobody -- `(p_other, body.changed)`, `who` the lord. His
        dominance weight stands, and the wound is one more deed of his.
    FALSIFIER: a called bluff leaves the weight unchanged (`success != before`, exactly 0 here)."""
    wound = "body.changed"
    assert wound in DOMINANCE_KINDS and wound in person_q.PAIRED_KINDS
    before_w, _ = _judging_world()
    _feared_lord(before_w)
    before = _rec(before_w, SPEAKER)
    assert before != 0.0

    won, _ = _judging_world()
    _feared_lord(won)
    won.persons[HEARER].ledger += [_claim("hit", HEARER, SPEAKER, wound, when=1),
                                   _seen("saw", HEARER, SPEAKER, NOBODY, when=1)]
    assert [c.id for c in person_q.suffered_deeds(won.persons[HEARER].ledger, SPEAKER)] == ["hit"]
    assert _rec(won, SPEAKER) == 0.0, "a called bluff left the dominance weight"
    # "NO NEWER THAN" is inclusive: a dominance deed deposited at exactly the bluff's tick is eroded too.
    kind_eq = _feared_lord(_judging_world()[0])
    won.persons[HEARER].ledger.append(_claim("eq", HEARER, SPEAKER, kind_eq, when=1))
    assert _rec(won, SPEAKER) == 0.0, "a deed at the bluff's own tick escaped erosion"

    lost, _ = _judging_world()
    _feared_lord(lost)
    lost.persons[HEARER].ledger += [_claim("hit", HEARER, NOBODY, wound, when=1),
                                    _seen("saw", HEARER, NOBODY, SPEAKER, when=1)]
    assert list(person_q.suffered_deeds(lost.persons[HEARER].ledger, SPEAKER)) == []
    only_new, _ = _judging_world()
    only_new.persons[HEARER].ledger += [_claim("hit", HEARER, NOBODY, wound, when=1),
                                        _seen("saw", HEARER, NOBODY, SPEAKER, when=1)]
    assert _rec(only_new, SPEAKER) != 0.0, "the wound is not one more deed of his"
    # Additive: the lord keeps his whole prior weight plus the new deed's (float sum order differs).
    assert math.isclose(_rec(lost, SPEAKER),
                        before + _rec(only_new, SPEAKER), rel_tol=1e-12)


def test_sc02_20_only_a_witness_is_moved_and_a_later_coercive_deed_counts_again():
    """A hearer only TOLD of the bluff holds no sighting, so no doer is named and nothing erodes; a
    dominance deed of the lord's AFTER the bluff counts again; a non-dominance deed is never eroded."""
    wound = "body.changed"
    told, _ = _judging_world()
    _feared_lord(told)
    before = _rec(told, SPEAKER)
    told.persons[HEARER].ledger.append(_claim("hit", HEARER, SPEAKER, wound, source="told_by",
                                              chain=(NOBODY,), when=1))
    assert _rec(told, SPEAKER) == before

    later, _ = _judging_world()
    kind = _feared_lord(later)
    later.persons[HEARER].ledger += [_claim("hit", HEARER, SPEAKER, wound, when=1),
                                     _seen("saw", HEARER, SPEAKER, NOBODY, when=1),
                                     _claim("again", HEARER, SPEAKER, kind, when=2)]
    # Only the re-earned deed counts: one firsthand claim at full confidence is its valence exactly.
    assert _rec(later, SPEAKER) == _lean(later, kind) != 0.0

    other, _ = _judging_world()
    gentle = _kind_with_lean(other, +1, among=_verbs.DEED_KINDS - DOMINANCE_KINDS)
    other.persons[HEARER].ledger += [_claim("g", HEARER, SPEAKER, gentle, when=0),
                                     _claim("hit", HEARER, SPEAKER, wound, when=1),
                                     _seen("saw", HEARER, SPEAKER, NOBODY, when=1)]
    assert _rec(other, SPEAKER) == _lean(other, gentle)


# ================================================================================================
# THE TWO MAGNITUDES' SWEEPS, EXECUTED (`H-215`, `H-216`; read off the register, not copied)
# ================================================================================================

def _sweep_of(hid):
    import yaml
    rows = yaml.safe_load(files.HOLE_REGISTER_YAML.read_text())["rows"]
    (row,) = [r for r in rows if r["id"] == hid]
    return row["sweep"], row["site"].split(",")[0].split()[-1]


def _bench(w, sign, count):
    """The bench's commit term at `count` kinds: the hearer's HOLDS commits about the speaker, the `count` kinds he leans on hardest in
    `sign`'s direction (a judge's commits to one kind count once, so a bigger room is more kinds, not more commits of one)."""
    return _hearer_commits(w, sign, count)


def _proofs(w, count, source="firsthand"):
    """`count` deed claims of the speaker's about his opponent, none of which the opponent mirrors."""
    kind = sorted(_verbs.DEED_KINDS - person_q.PAIRED_KINDS)[0]
    for i in range(count):
        w.persons[SPEAKER].ledger.append(_claim(f"proof{i}", SPEAKER, PARTY, kind, source=source))


def _obstacle_at(w, pool):
    """`(ob, terms)` the module composes for the speaker's record at `pool` (the cap rises with the pool, so a pool of 8 leaves a
    hostile bench room to raise it; the shipped actor's own pool sits at the cap already)."""
    return _module().obstacle(replace(_input(w), pool=pool))


def _partial_or_better(w, pool):
    """P(Partial or better) on the closed form of the one sampler, for the speaker's record taken at `pool`: the module's obstacle and
    the roll's own boost (`net_boost`) of the host's leverage. Read, never rolled."""
    inp = replace(_input(w), pool=pool)
    ob, _terms = _module().obstacle(inp)
    return 1.0 - band_odds(pool, ob, net_boost(inp.leverage, pool))[0]


def test_sc02_the_reception_gain_and_proof_level_sweeps_run_and_the_control_is_the_nothing_arm():
    """B05.17: each declared point of `H-215` and `H-216` is run through the real adapter. `reception_gain` 0 is its CONTROL: a hostile
    bench raises the obstacle by nothing and a favourable one brings no levels, and each larger point moves them strictly further.
    `proof_level` None is its control (a proof brings nothing) and each named level above it brings strictly more leverage."""
    gains, _site = _sweep_of("H-215")
    assert _site == "reception_gain" and len(gains) == 3 and 0 in gains, gains
    hostile_ob, favour_lev = [], []
    for gain in sorted(gains):
        h, _d = _judging_world(reception_gain=gain)
        _bench(h, -1, 1)
        hostile_ob.append(_obstacle_at(h, 8)[0])
        f, _d = _judging_world(reception_gain=gain)
        _bench(f, +1, 3)
        favour_lev.append(_input(f).leverage)
    n, _d = _judging_world(reception_gain=0)
    assert hostile_ob[0] == _obstacle_at(n, 8)[0] and favour_lev[0] == 0.0, (hostile_ob, favour_lev)       # the control: nothing of the room
    assert hostile_ob[0] < hostile_ob[1] < hostile_ob[2] and favour_lev[0] < favour_lev[1] < favour_lev[2], (hostile_ob, favour_lev)
    levels, fixture = _sweep_of("H-216")
    assert fixture == "proof_level" and len(levels) == 3 and None in levels, levels
    lev = []
    for level in levels:
        w, _d = _judging_world(proof_level=level)
        _proofs(w, 4)
        lev.append(_input(w).leverage)
    assert lev[0] == 0.0 and lev[0] < lev[1] < lev[2], (levels, lev)


# ================================================================================================
# B05.17 -- WHAT THE SPEAKER BRINGS IS LEVERAGE; THE HOSTILE ROOM IS A TERM (PES-A, OBS §4 step 1b)
# ================================================================================================

# The closed form is read over ten pools from the shipped `pool_floor` up, and never below one die: a pool of nothing rolls nothing and
# `net_boost` is `sqrt(pool)` of its shift, so at pool 0 NO leverage moves the odds (a true dead zone by construction, observed below,
# not a cell in play). At the control floor (0) the range is 1 to 10; B05.23 ships `pool_floor` 5 (CAP B2), so it is 5 to 14 and no
# pool in play is smaller.
def _pools():
    low = max(1, int(DEFAULT_FIXTURES.get("pool_floor")))
    return list(range(low, low + 10))


def test_the_pool_range_reads_the_shipped_pool_floor():
    """B05.23 (CAP B2; T13 commit 2): the range the falsifiers below read starts at the shipped `pool_floor`, 5 at the calibrated arm."""
    assert DEFAULT_FIXTURES.get("pool_floor") == 5
    assert _pools() == list(range(5, 15))


def test_a_pool_of_nothing_takes_no_shift():
    """The cell excluded from the range below, observed: at pool 0 the boost is 0 whatever the leverage (the closed form returns 1 or 0)."""
    w, _d = _judging_world()
    _bench(w, +1, 12)
    _proofs(w, 4)
    assert _input(w).leverage > 0.0
    assert net_boost(_input(w).leverage, 0) == 0.0
    assert _partial_or_better(w, 0) == 0.0


def test_each_proof_strictly_raises_partial_or_better_at_every_pool():
    """FALSIFIER (PES-A): a cell in which adding a proof leaves the odds unchanged, at any pool from the floor. Before a hostile, a
    neutral and a friendly bench, with `proof_level` set, each added proof strictly raises P(Partial or better)."""
    checked = 0
    for bench, count in (("hostile", 8), ("neutral", 0), ("friendly", 12)):
        for pool in _pools():
            odds = []
            for held in (0, 1, 2, 3):
                w, _d = _judging_world(proof_level="minor")
                if count:
                    _bench(w, -1 if bench == "hostile" else +1, count)
                _proofs(w, held)
                odds.append(_partial_or_better(w, pool))
            assert odds[0] < odds[1] < odds[2] < odds[3], (bench, pool, odds)
            checked += 1
    assert checked == 3 * len(_pools()) and len(_pools()) == 10, checked


def test_favour_strictly_raises_partial_or_better():
    """FALSIFIER (PES-A): a unit of favour that leaves the odds unchanged. A friendlier bench (more whole units of `reception_gain x
    reception`) strictly raises P(Partial or better) at every pool, with `favour_level` set."""
    checked = 0
    for pool in _pools():
        odds = []
        for units in (0, 1, 3, 6):
            w, _d = _judging_world(favour_level="major")
            if units:
                _hearer_commits_to(w, +1, units)                             # a reception of at least `units`, under `units + 1`
            odds.append(_partial_or_better(w, pool))
        assert odds[0] < odds[1] < odds[2] < odds[3], (pool, odds)
        checked += 1
    assert checked == 10


def test_hostile_bench_raises_the_obstacle_only():
    """A hostile bench is a TERM (the `reception` member of `obstacle_terms`): it raises the obstacle by `reception_gain x |reception|`
    and brings no leverage; a friendly one lowers no obstacle. Read at pool 8, where the cap leaves the room to rise."""
    neutral, _d = _judging_world()
    hostile, _d = _judging_world()
    friendly, _d = _judging_world()
    _bench(hostile, -1, 1)
    _bench(friendly, +1, 3)
    r = _rec(hostile, SPEAKER, SPEAKER)
    assert r < 0.0 < _rec(friendly, SPEAKER, SPEAKER)
    gain = hostile.fixtures.get("reception_gain")
    (ob_n, t_n), (ob_h, t_h), (ob_f, t_f) = (_obstacle_at(w, 8) for w in (neutral, hostile, friendly))
    assert dict(t_n)["reception"] == 0.0 and dict(t_f)["reception"] == 0.0, (t_n, t_f)
    assert dict(t_h)["reception"] == -gain * r > 0.0 and ob_h > ob_n and ob_h - ob_n == dict(t_h)["reception"], (t_h, ob_h, ob_n)
    assert "room" not in dict(t_h) and sum(v for _, v in t_h) == ob_h
    assert ob_f == ob_n                                                    # a friendly bench does not touch the obstacle
    assert _input(hostile).leverage == _input(neutral).leverage == 0.0     # and a hostile one brings the speaker nothing
    assert _input(friendly).leverage > 0.0


def test_control_levels_none_moves_nothing():
    """CONTROL: with `proof_level` and `favour_level` None a held proof and a friendly bench move NOTHING (leverage and obstacle exactly
    the nothing-held record's, the odds equal at every pool), and the same world at the shipped levels moves them (the control can fail)."""
    bare, _d = _judging_world(proof_level=None, favour_level=None)
    held, _d = _judging_world(proof_level=None, favour_level=None)
    _bench(held, +1, 12)
    _proofs(held, 4)
    live, _d = _judging_world()
    _bench(live, +1, 12)
    _proofs(live, 4)
    assert world_q.proofs(held, SPEAKER, PARTY, world_q.judging_set(held, "Hh")) == 4.0 and _rec(held, SPEAKER, SPEAKER) > 1.0
    assert _input(held).leverage == _input(bare).leverage == 0.0
    assert _ob(held) == _ob(bare)
    for pool in _pools():
        assert _partial_or_better(held, pool) == _partial_or_better(bare, pool), pool
    assert _input(live).leverage > 0.0 and _partial_or_better(live, 4) > _partial_or_better(bare, 4)


def test_sc02_20_the_route_roster_names_only_deed_kinds():
    assert DOMINANCE_KINDS and DOMINANCE_KINDS <= _verbs.DEED_KINDS, sorted(DOMINANCE_KINDS)
    assert DOMINANCE_KINDS & person_q.PAIRED_KINDS, "no dominance kind has a patient: no bluff is callable"


# ================================================================================================
# B24.02 (F8, option B) -- THE ROOM READS THE ACTOR'S OWN LEDGER AND THE BENCH'S PUBLIC COMMITS, NEVER ANOTHER LEDGER
# ================================================================================================

J1, J2 = HEARER, NOBODY            # the two seats of the bench over `Hh`; `speaker` S = p_low, `opponent` O = p_mid


def _worlds_bench():
    """`_judging_world` with a second seat at the Duke's rung: the bench over `Hh` is {J1, J2}, both with the pursuit that makes a deed lean."""
    w, _d = _judging_world()
    w.offices["off_second"] = Office("off_second", "Duke", "D", ["determine"], faction="Valorsmark")
    w.add_tenure(Tenure("t_second", J2, "off_second", "hold", since=0))
    w.persons[J2].pursuits = {PURSUIT: 1.0}
    assert sorted(world_q.judging_set(w, "Hh")) == sorted([J1, J2]), world_q.judging_set(w, "Hh")
    return w


def _world_a():
    """WORLD A (the opponent's ledger and the judges' ledgers only; nobody has committed): J1 and J2 each hold one firsthand deed claim of S's
    that they disvalue, and O holds a claim with the same (subject, predicate) as S's one proof against O."""
    w = _worlds_bench()
    hostile = _kind_with_lean(w, -1)
    proof_kind = sorted(_verbs.DEED_KINDS - person_q.PAIRED_KINDS)[0]
    for j in (J1, J2):
        w.persons[j].ledger.append(_claim(f"a_{j}", j, SPEAKER, hostile))
    w.persons[SPEAKER].ledger.append(_claim("a_proof", SPEAKER, PARTY, proof_kind))
    w.persons[PARTY].ledger.append(_claim("a_mirror", PARTY, PARTY, proof_kind))
    return w, hostile, proof_kind


def _shifted_axes(w, who):
    fx = w.fixtures
    return person_q.projected_axes(w.persons[who], fx.get("scar_weight_shift"), hold=fx.get("scar_hold"), mass=fx.get("scar_primary_mass"))


def _room(w):
    bench = tuple(world_q.judging_set(w, "Hh"))
    return world_q.reception(w, SPEAKER, bench, SPEAKER), world_q.proofs(w, SPEAKER, PARTY, bench)


def test_sc02_world_a_no_ledger_but_the_actors_own_moves_the_room():
    """WORLD A: the judges' ledgers hold S's deeds (a hostile bench by the base's reading) and O's ledger mirrors S's proof, and no one has
    committed. S is the actor of a `speak` (the speaker, off the bench): `reception == 0.0` exactly and `proofs == remove_weight`, unmirrored.
    FALSIFIER: A's reception non-zero (a judge's ledger read) or A's proofs zero (the opponent's ledger read); a planted `h.ledger` in the
    commit term's place reddens it."""
    w, hostile, _pk = _world_a()
    assert all(person_q.deed_valence(_shifted_axes(w, j), _claim("p", j, SPEAKER, hostile)) < 0.0 for j in (J1, J2))   # the control: both judges' ledgers lean, so a read of them would move it
    reception, proofs = _room(w)
    assert reception == 0.0
    assert proofs == world_q.remove_weight("firsthand") > 0.0


def test_sc02_world_b_the_bench_commit_moves_the_room_and_the_opponents_commit_mirrors_the_proof():
    """WORLD B: A plus J1's live HOLDS commit to a Proposition that S did the hostile kind (value True) and O's live commit to a Proposition on the
    proof's (subject, predicate), a denial. `reception == deed_valence(projected_axes(J1, shift), P) < 0` exactly; `proofs == 0.0`.
    FALSIFIER: B's room equal to A's."""
    w, hostile, proof_kind = _world_a()
    a = _room(w)
    p = _commit(w, J1, SPEAKER, hostile)
    _commit(w, PARTY, PARTY, proof_kind, value=False)
    reception, proofs = _room(w)
    assert reception == person_q.deed_valence(_shifted_axes(w, J1), p) < 0.0
    assert proofs == 0.0
    assert (reception, proofs) != a


def test_sc02_world_c_the_actors_own_ledger_counts_through_the_own_term_and_a_second_judges_ledger_moves_nothing():
    """WORLD C: A with the actor J1 himself (a `determine` by J1, CP-T05-01 not yet moving the prize: the Query is called directly). J1's own
    claim counts through the own term at `deed_term`'s value; J2's identical ledger claim does not move the total."""
    w, hostile, _pk = _world_a()
    bench = tuple(world_q.judging_set(w, "Hh"))
    own = world_q.reception(w, SPEAKER, bench, J1)
    assert own == person_q.deed_term(w.persons[J1], _shifted_axes(w, J1), next(c for c in w.persons[J1].ledger if c.id == f"a_{J1}")) == _lean(w, hostile) < 0.0
    w.persons[J2].ledger.append(_claim("c_j2_more", J2, SPEAKER, hostile))
    assert world_q.reception(w, SPEAKER, bench, J1) == own, "a second judge's ledger moved the room"
    assert world_q.reception(w, SPEAKER, bench, J2) != own and world_q.reception(w, SPEAKER, bench, SPEAKER) == 0.0   # the control: it is the ACTOR's own ledger that is read


def test_sc02_an_ended_commit_reads_as_no_commit():
    """The ended commit: World B with J1's and O's commits closed (`until` set) reads as World A."""
    w, hostile, proof_kind = _world_a()
    a = _room(w)
    _commit(w, J1, SPEAKER, hostile, live=False)
    _commit(w, PARTY, PARTY, proof_kind, value=False, live=False)
    assert _room(w) == a == (0.0, world_q.remove_weight("firsthand"))


def test_sc02_one_judge_two_propositions_of_one_key_count_once():
    """One judge's commits to two Propositions of the same (subject, predicate, value) count once; a second judge's commit counts as his own."""
    w, hostile, _pk = _world_a()
    one = _commit(w, J1, SPEAKER, hostile)
    _commit(w, J1, SPEAKER, hostile)
    assert _room(w)[0] == person_q.deed_valence(_shifted_axes(w, J1), one) < 0.0
    _commit(w, J2, SPEAKER, hostile)
    assert _room(w)[0] == person_q.deed_valence(_shifted_axes(w, J1), one) + person_q.deed_valence(_shifted_axes(w, J2), one)


def test_sc02_only_a_holds_deed_of_value_true_by_a_person_about_the_target_counts_in_the_room():
    """The commit term's own rules: an `OUGHT` commit, a denial (value False), a predicate outside `DEED_KINDS`, a commit about someone else and a
    commit to a Proposition that does not exist count 0; the HOLDS deed about the target beside them counts."""
    w, hostile, _pk = _world_a()
    _commit(w, J1, SPEAKER, hostile, mood="OUGHT")
    _commit(w, J1, SPEAKER, hostile, value=False)
    _commit(w, J1, SPEAKER, "not_a_deed_kind")
    _commit(w, J1, PARTY, hostile)
    w.add_tenure(Tenure("t_ghost", J1, "prop_nowhere", "commit", 0))
    assert _room(w)[0] == 0.0
    p = _commit(w, J1, SPEAKER, hostile)
    assert _room(w)[0] == person_q.deed_valence(_shifted_axes(w, J1), p) < 0.0
