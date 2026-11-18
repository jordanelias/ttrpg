"""v9 SC-02 `22a`, piece 1 -- proceedings PHASE 3 steps 17, 18 and 20 (`19_PLAN.md`, intent only):
`reception` (the bench's ledgers about the speaker, resolver-side), `proofs` (weighed by remove, discounted
by the mirror) and route erosion (the single called bluff, inside reception).

WHAT IS BUILT, asked of the real host builder (`seam/wrappers/sigma.py`), the real module
(`modules/social_contest/roll.py::obstacle`) and the real fold on a HAND-BUILT world (`probes.tiny_world`
through `test_u7_remit._world`: `p_high` holds `off_duke`, whose bench sits over `Hh`; the speaker `p_low`
and his party `p_mid` live in `Hh`; `p_other` lives there and sits on no bench):
  * `world_q.reception(w, speaker, venue)` -- each bench member's own deed claims about the speaker,
    weighted by `remove_weight(source)` x decayed confidence x the member's valence (arm 1, the alignment
    table; arm 2 was never authored and the sweep is open, `hole_register.yaml` H-215), summed; `reception_gain` scales it: its
    hostile half into the obstacle (the `reception` member), its favourable half into `favour` levels (`H-215`, B05.17);
  * `world_q.proofs(w, speaker, opponent, venue)` -- the speaker's deed claims about the opponent weighed by
    remove, zero for any the opponent mirrors (same subject and predicate); `proof_level` (`H-216`, B05.17: a proof is a
    named level of leverage, never an obstacle reduction);
  * route erosion -- `rosters.yaml: standing_routes`: a hearer who saw a dominance-route deed done TO the
    speaker zeroes every dominance-route deed of his no newer than it.

THE FALSIFIERS (`19_PLAN.md` :537, :550, :578), each an assertion below that observes its failure:
  * step 17: a bench's obstacle invariant under a change to a member's ledger; the Query reachable from a
    decision -- `test_sc02_17_...`;
  * step 18: the mirrored proof moves the obstacle -- `test_sc02_18_...`;
  * step 20: a called bluff leaves the weight unchanged -- `test_sc02_20_...`.
"""

from __future__ import annotations

import ast
import math
import random
from pathlib import Path

from dataclasses import replace

from engine.dice_engine.sigma_leverage import LEVEL_SIGMA, band_odds, levels_to_net_sigma, net_boost

from ..data import files
from ..data.fixtures import DEFAULT_FIXTURES
from ..data.rosters import DOMINANCE_KINDS, REMOVE_ORDINAL, SEEN_PREDICATE
from ..data import verbs as _verbs
from ..epistemic import Seen
from ..queries import person_q, world_q
from ..seam.wrappers import sigma
from ..state.carriers import Act, Claim
from .test_sc01_obstacle_ceiling import _module
from .test_u7_remit import _fold, _kinds, _open, _world

SPEAKER, PARTY, HEARER, NOBODY = "p_low", "p_mid", "p_high", "p_other"
PRIZE = "a matter"
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


def _ob(w, actor=SPEAKER, subject=PARTY):
    """The composed obstacle of one `speak`'s draw, through the real adapter and module entry."""
    out = sigma.resolve(w, [actor, subject], ["root"], PRIZE, verb="speak", subject=subject,
                        rng=random.Random(0), rung=world_q.place_of(w, actor))
    assert out["status"] == "RESOLVED", out
    return out["ob"]


def _input(w, actor=SPEAKER, subject=PARTY):
    return sigma.contest_input(w, [actor, subject], verb="speak", subject=subject,
                               room=world_q.place_of(w, actor))


# ================================================================================================
# STEP 17 -- RECEPTION
# ================================================================================================

def test_sc02_17_two_benches_differing_only_in_one_ledger_band_differently_for_the_same_draw():
    """`19_PLAN.md` step 17's artifact: identical seats and convictions, one member's ledger differs, and
    the same seeded `speak` resolves at different bands. FALSIFIER: the obstacle invariant under the
    ledger change (asserted on every draw, and on the band over the sweep)."""
    plain, d_plain = _judging_world()
    heard, d_heard = _judging_world()
    kind = _kind_with_lean(heard, +1)
    n = math.ceil(1.0 / _lean(heard, kind)) + 1        # enough favour to reach the Ob floor from 2
    for i in range(n):
        heard.persons[HEARER].ledger.append(_claim(f"fav{i}", HEARER, SPEAKER, kind))
    for w, d in ((plain, d_plain), (heard, d_heard)):
        assert _kinds(_fold(w, d, _open("oc"))) == ["case.opened"]
    assert world_q.reception(plain, SPEAKER, "Hh") == 0.0
    assert world_q.reception(heard, SPEAKER, "Hh") > 0.0
    # B05.17: the favourable bench is LEVERAGE (`favour`), not a lower obstacle: what the speaker brings rises, what stands against him does not.
    assert _input(heard).leverage > _input(plain).leverage, (_input(heard).leverage, _input(plain).leverage)
    assert _ob(heard) == _ob(plain), (_ob(heard), _ob(plain))
    differ = checked = 0
    for i in range(40):
        a = _fold(plain, d_plain, Act(id=f"sp{i}", actor=SPEAKER, verb="speak", payload={"subject": PARTY}))
        b = _fold(heard, d_heard, Act(id=f"sp{i}", actor=SPEAKER, verb="speak", payload={"subject": PARTY}))
        assert len(a) == len(b) == 1 and a[0].degree and b[0].degree, (_kinds(a), _kinds(b))
        differ += a[0].degree != b[0].degree
        checked += 1
    assert checked == 40
    assert differ >= 1, "no draw banded differently: the bench's ledger did not reach the outcome"


def test_sc02_17_a_ledger_off_the_bench_moves_nothing():
    """THE CONTROL: the same claims in a person who sits on no bench over `Hh` leave reception at 0 and
    the obstacle at its base, so what moved it above is the BENCH's ledger, not any ledger."""
    w, _d = _judging_world()
    w.persons[NOBODY].pursuits = {PURSUIT: 1.0}
    kind = _kind_with_lean(w, +1)
    base = _ob(w)
    for i in range(5):
        w.persons[NOBODY].ledger.append(_claim(f"off{i}", NOBODY, SPEAKER, kind))
    assert world_q.reception(w, SPEAKER, "Hh") == 0.0
    assert _ob(w) == base


def test_sc02_17_a_told_claim_moves_the_obstacle_strictly_less_than_the_same_claim_firsthand():
    """Step 17's second artifact, over the ordinal of remove: firsthand > knot-sourced > told > inferred,
    each strictly, and every rank still counts (B05.17: read as the speaker's LEVERAGE, `favour` levels, above the
    no-claim base; the name keeps its first word, the reading moved from the obstacle). A unit of favour is whole, so
    the bench holds enough claims that each rank's weight is whole units apart."""
    lev = {}
    for source in REMOVE_ORDINAL:
        w, _d = _judging_world()
        kind = _kind_with_lean(w, +1)
        chain = ("p_king",) if source == "told_by" else ()
        for i in range(math.ceil(8.0 / _lean(w, kind))):
            w.persons[HEARER].ledger.append(_claim(f"c{i}", HEARER, SPEAKER, kind, source=source, chain=chain))
        lev[source] = _input(w).leverage
    w0, _d = _judging_world()
    base = _input(w0).leverage
    ranked = [lev[s] for s in REMOVE_ORDINAL]
    assert ranked == sorted(ranked, reverse=True) and len(set(ranked)) == len(ranked), lev
    assert lev["firsthand"] > lev["told_by"] > base, (lev, base)
    assert min(ranked) > base, (lev, base)                                   # even the most removed rank counts


def test_sc02_17_decayed_confidence_counts_less_and_a_hostile_bench_reads_negative():
    w, _d = _judging_world()
    kind = _kind_with_lean(w, +1)
    w.persons[HEARER].ledger.append(_claim("full", HEARER, SPEAKER, kind))
    full = world_q.reception(w, SPEAKER, "Hh")
    w.persons[HEARER].ledger[-1] = _claim("half", HEARER, SPEAKER, kind, conf=50)
    assert world_q.reception(w, SPEAKER, "Hh") == full / 2
    hostile = _kind_with_lean(w, -1)
    w.persons[HEARER].ledger[-1] = _claim("bad", HEARER, SPEAKER, hostile)
    assert world_q.reception(w, SPEAKER, "Hh") < 0.0
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
            found[node.name] = (first.arg, ast.unparse(first.annotation) if first.annotation else None)
    assert found == {"reception": ("w", "World"), "proofs": ("w", "World")}, found


def test_sc02_17_only_a_prize_a_room_hears_reads_the_room(monkeypatch):
    """`heard_by: bench` is on `a matter` alone: a `tell` (`a standing`) or an inquiry by the same actor
    at the same rung carries the record's no-room defaults, so every other social roll is as it was."""
    w, _d = _judging_world()
    kind = _kind_with_lean(w, +1)
    w.persons[HEARER].ledger.append(_claim("c1", HEARER, SPEAKER, kind))
    seen = {}
    real = sigma._read_social_roll

    def spy(*a, **kw):
        built = real(*a, **kw)
        seen[kw.get("verb")] = built[0]
        return built
    monkeypatch.setattr(sigma, "_read_social_roll", spy)
    for prize, verb in ((PRIZE, "speak"), ("a standing", "tell")):
        sigma.resolve(w, [SPEAKER, PARTY], ["root"], prize, verb=verb, subject=PARTY,
                      rng=random.Random(0), rung="Hh")
    assert seen["speak"].reception > 0.0
    assert seen["tell"].reception == 0.0 and seen["tell"].reception_gain == 0.0, seen["tell"]


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
    holds nothing, so reception is 0 and only the proofs source moves the leverage.
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
        assert world_q.reception(w, SPEAKER, "Hh") == 0.0
        owed = levels_to_net_sigma([level] * int(4 * world_q.remove_weight(source) + 0.5))
        assert owed > 0.0 and _input(w).leverage == base + owed, (source, _input(w).leverage, owed)
        assert _ob(w) == base_ob, (source, _ob(w), base_ob)                 # the obstacle is not where a proof acts
        # NEAR-MISSES DO NOT MIRROR: the same predicate about another subject, and the same subject
        # under another predicate, leave the proof standing (the mirror keys on BOTH).
        other_kind = next(k for k in sorted(_verbs.DEED_KINDS - person_q.PAIRED_KINDS) if k != kind)
        w.persons[PARTY].ledger += [_claim("near_a", PARTY, NOBODY, kind),
                                    _claim("near_b", PARTY, PARTY, other_kind)]
        assert _input(w).leverage == base + owed, "a near-miss mirrored a proof"
        # THE MIRROR: the opponent holds a claim of the same subject and predicate -> exactly zero.
        w.persons[PARTY].ledger.append(_claim("mirror", PARTY, PARTY, kind))
        assert world_q.proofs(w, SPEAKER, PARTY, "Hh") == 0.0
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
    assert world_q.proofs(w, SPEAKER, None, "Hh") == 0.0
    # A NON-PERSON OPPONENT holds no ledger, so nothing of his mirrors a proof: a deed claim the speaker
    # holds about the rung `Hh` itself is counted whole (observable: it is not zero).
    w2, _d2 = _judging_world()
    assert "Hh" not in w2.persons
    w2.persons[SPEAKER].ledger.append(_claim("pr", SPEAKER, "Hh", kind))
    assert world_q.proofs(w2, SPEAKER, "Hh", "Hh") == world_q.remove_weight("firsthand") > 0.0


def test_sc02_18_proofs_are_spent_on_a_bench_and_never_on_an_empty_room():
    """With nobody on the bench there is no one to spend a proof on (`reception`'s own rule): the same
    held proof counts on `Hh` and counts zero with no venue (a placeless speaker) -- the control."""
    w, _d = _judging_world()
    kind = sorted(_verbs.DEED_KINDS - person_q.PAIRED_KINDS)[0]
    w.persons[SPEAKER].ledger.append(_claim("pf", SPEAKER, PARTY, kind))
    assert world_q.proofs(w, SPEAKER, PARTY, "Hh") == world_q.remove_weight("firsthand") > 0.0
    assert world_q.proofs(w, SPEAKER, PARTY, None) == 0.0
    assert world_q.judging_set(w, "Hh") == [HEARER]
    # the only seated person IS the speaker: nobody else is in the room
    w.persons[HEARER].ledger.append(_claim("pf2", HEARER, PARTY, kind))
    assert world_q.proofs(w, HEARER, PARTY, "Hh") == 0.0


def test_sc02_17_a_man_does_not_receive_himself():
    """The speaker is excluded from his own bench: a seated person's reception of HIMSELF is 0 though his
    ledger holds deed claims of his own that lean (CONTROL: the same claims read non-zero when the
    speaker is someone else and the holder is on the bench)."""
    w, _d = _judging_world()
    kind = _kind_with_lean(w, +1)
    w.persons[HEARER].ledger.append(_claim("mine", HEARER, HEARER, kind))
    assert world_q.reception(w, HEARER, "Hh") == 0.0
    w.persons[HEARER].ledger.append(_claim("his", HEARER, SPEAKER, kind))
    assert world_q.reception(w, SPEAKER, "Hh") != 0.0


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
    before = world_q.reception(before_w, SPEAKER, "Hh")
    assert before != 0.0

    won, _ = _judging_world()
    _feared_lord(won)
    won.persons[HEARER].ledger += [_claim("hit", HEARER, SPEAKER, wound, when=1),
                                   _seen("saw", HEARER, SPEAKER, NOBODY, when=1)]
    assert [c.id for c in person_q.suffered_deeds(won.persons[HEARER].ledger, SPEAKER)] == ["hit"]
    assert world_q.reception(won, SPEAKER, "Hh") == 0.0, "a called bluff left the dominance weight"
    # "NO NEWER THAN" is inclusive: a dominance deed deposited at exactly the bluff's tick is eroded too.
    kind_eq = _feared_lord(_judging_world()[0])
    won.persons[HEARER].ledger.append(_claim("eq", HEARER, SPEAKER, kind_eq, when=1))
    assert world_q.reception(won, SPEAKER, "Hh") == 0.0, "a deed at the bluff's own tick escaped erosion"

    lost, _ = _judging_world()
    _feared_lord(lost)
    lost.persons[HEARER].ledger += [_claim("hit", HEARER, NOBODY, wound, when=1),
                                    _seen("saw", HEARER, NOBODY, SPEAKER, when=1)]
    assert list(person_q.suffered_deeds(lost.persons[HEARER].ledger, SPEAKER)) == []
    only_new, _ = _judging_world()
    only_new.persons[HEARER].ledger += [_claim("hit", HEARER, NOBODY, wound, when=1),
                                        _seen("saw", HEARER, NOBODY, SPEAKER, when=1)]
    assert world_q.reception(only_new, SPEAKER, "Hh") != 0.0, "the wound is not one more deed of his"
    # Additive: the lord keeps his whole prior weight plus the new deed's (float sum order differs).
    assert math.isclose(world_q.reception(lost, SPEAKER, "Hh"),
                        before + world_q.reception(only_new, SPEAKER, "Hh"), rel_tol=1e-12)


def test_sc02_20_only_a_witness_is_moved_and_a_later_coercive_deed_counts_again():
    """A hearer only TOLD of the bluff holds no sighting, so no doer is named and nothing erodes; a
    dominance deed of the lord's AFTER the bluff counts again; a non-dominance deed is never eroded."""
    wound = "body.changed"
    told, _ = _judging_world()
    _feared_lord(told)
    before = world_q.reception(told, SPEAKER, "Hh")
    told.persons[HEARER].ledger.append(_claim("hit", HEARER, SPEAKER, wound, source="told_by",
                                              chain=(NOBODY,), when=1))
    assert world_q.reception(told, SPEAKER, "Hh") == before

    later, _ = _judging_world()
    kind = _feared_lord(later)
    later.persons[HEARER].ledger += [_claim("hit", HEARER, SPEAKER, wound, when=1),
                                     _seen("saw", HEARER, SPEAKER, NOBODY, when=1),
                                     _claim("again", HEARER, SPEAKER, kind, when=2)]
    # Only the re-earned deed counts: one firsthand claim at full confidence is its valence exactly.
    assert world_q.reception(later, SPEAKER, "Hh") == _lean(later, kind) != 0.0

    other, _ = _judging_world()
    gentle = _kind_with_lean(other, +1, among=_verbs.DEED_KINDS - DOMINANCE_KINDS)
    other.persons[HEARER].ledger += [_claim("g", HEARER, SPEAKER, gentle, when=0),
                                     _claim("hit", HEARER, SPEAKER, wound, when=1),
                                     _seen("saw", HEARER, SPEAKER, NOBODY, when=1)]
    assert world_q.reception(other, SPEAKER, "Hh") == _lean(other, gentle)


# ================================================================================================
# THE TWO MAGNITUDES' SWEEPS, EXECUTED (`H-215`, `H-216`; read off the register, not copied)
# ================================================================================================

def _sweep_of(hid):
    import yaml
    rows = yaml.safe_load(files.HOLE_REGISTER_YAML.read_text())["rows"]
    (row,) = [r for r in rows if r["id"] == hid]
    return row["sweep"], row["site"].split(",")[0].split()[-1]


def _bench(w, sign, count):
    """`count` claims of the hearer's about the speaker, each of the kind he leans on hardest in `sign`'s direction."""
    kind = _kind_with_lean(w, sign)
    for i in range(count):
        w.persons[HEARER].ledger.append(_claim(f"bench{sign:+d}_{i}", HEARER, SPEAKER, kind))
    return kind


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
                kind = _kind_with_lean(w, +1)
                _bench(w, +1, math.ceil(units / _lean(w, kind)))            # a reception of at least `units`, under `units + 1`
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
    r = world_q.reception(hostile, SPEAKER, "Hh")
    assert r < 0.0 < world_q.reception(friendly, SPEAKER, "Hh")
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
    assert world_q.proofs(held, SPEAKER, PARTY, "Hh") == 4.0 and world_q.reception(held, SPEAKER, "Hh") > 1.0
    assert _input(held).leverage == _input(bare).leverage == 0.0
    assert _ob(held) == _ob(bare)
    for pool in _pools():
        assert _partial_or_better(held, pool) == _partial_or_better(bare, pool), pool
    assert _input(live).leverage > 0.0 and _partial_or_better(live, 4) > _partial_or_better(bare, 4)


def test_sc02_20_the_route_roster_names_only_deed_kinds():
    assert DOMINANCE_KINDS and DOMINANCE_KINDS <= _verbs.DEED_KINDS, sorted(DOMINANCE_KINDS)
    assert DOMINANCE_KINDS & person_q.PAIRED_KINDS, "no dominance kind has a patient: no bluff is callable"
