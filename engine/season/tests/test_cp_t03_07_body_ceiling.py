"""v11 CP-T03-07 -- A LASTING MARK: THE BODY CEILING (P32).

(i) `Person.body_ceiling: int`, built at `condition_scale`. (ii) A party who survives a fight at the engine's deepest
gate short of felling -- `wounds >= max_wounds` on his lifted tracker -- has his ceiling fall to one below the next
`band_floors["body"]` floor beneath it (`loop/effects_combat.py::marked_ceiling`: 1000 -> 799 -> 499 -> 99, as many
marks as the body has floors), and his written body is held under it. (iii) Every raiser of `body` heals toward
`body_ceiling`: `_eff_tend` at HEAD (the one raiser; CP-T10-04 is unbuilt). (iv) `body_mark_model in {none,
deepest_gate}`, SHIPPED `deepest_gate` on REM-52's precedent (`body_step`) [ASSUMPTION; medium; Jordan to correct;
revert: none].

  FALSIFIER: a survivor at `wounds == max_wounds` holds 799; `tend` on him at body 250 restores him to 799 where the
  same `tend` on an unmarked man restores 1000 (`_eff_tend` at HEAD restores the WHOLE headroom: there is no
  `tend_share` -- that term is CP-T10-04's, unbuilt, so the home's 524/625 arithmetic is not this item's; AM-C-06
  moved it to CP-T10-04's exit). His `budget` sits one below whole (799 is under the 800 floor).
  MUTATION (executed below): a `tend` that heals to `condition_scale` lifts him past 799 -- red.
  ASYMMETRY GUARD (`CLAUDE.md` §0.1 pt 1, `tests/valoria/test_morale_write_sweep.py`'s shape): every bare `body`
  write outside tests and harness is registered in `_BODY_WRITES` with how it stands to the ceiling; a RAISER's
  function must read `body_ceiling` and not `condition_scale`. A new write fails until it is registered.
  CONTROL: `body_mark_model: none` marks nobody. The field is a SCHEMA mover (every Person's canonical encoding), so
  `revert_cp_t03_07` drops it from the encoding as well and reproduces every pre-item hash.
"""
from __future__ import annotations

import ast
import pathlib
import re
from dataclasses import fields

import pytest

from ..data.fixtures import DEFAULT_FIXTURES
from ..data.matrix import MATRIX, Step, WriteClass
from ..data.rosters import BODY_MARK_MODELS, WOUNDED
from ..data.verbs import VERB_TABLE
from ..decision.budget import body_band_penalty
from ..harness import probes as P
from ..harness.populated import build_realm, run
from ..loop import effects_combat as EC
from ..loop.driver import SeasonDriver, mint_token
from ..loop.effects_shared import EFFECTS
from ..seam import Resolution, degree_of
from ..state import world as W
from ..state.carriers import Act, Person
from ._scar_helpers import party_state
from .test_in12_step9 import _tend_acts, _world
from .test_in10_record_operands import _resolve

ACTOR, SUBJECT = "p_low", "p_mid"          # `tiny_world`: co-located, a `fight` between them is admitted
CEILING = "body_ceiling"

#: 1-season hashes before this item (ed983b6a, = CP-T03-04's POST_ITEM) and after it. `build_realm(0)`:
#: 7266f56bea4e3d75705f5e88eec1b2e1 -> 600d8b27147478e158553552cc1409a5 (the schema).
#: Seeds 1 and 2 of both are the post-B10-11b reading (`reading @4b334f2a`), re-recorded by the batch pin commit: PC-20 (1)
#: (the head-weighted strike impact, `K_STR_HEAD`) moves a one-season run that reaches `strike_impact`; seed 0 calls none.
#: Was, before that pin commit: PRE_ITEM 07634b99... / 1cc4370d...; POST_ITEM fc3201f3... / 6da144ff...; CONTROL seed 2 702d9074....
#: B10-13 batch pin commit: PRE_ITEM was b2dde1fc... / c58b1a7e... / 5518f31c... (= CP-T03-04's POST_ITEM, re-recorded with it);
#: POST_ITEM was eb2919ae... / c4ba7a75... / c72aa6fe...; CONTROL seed 2 was 7ee0f657....
#: B10-12 pin commit (CR-24 `field_winner_casualties: engine` and MB-07r's support cap, both shipped, move a one-season
#: realm that fights; control: both reverted reads the old pins): seed 2 PRE_ITEM was 6078a950... (= CP-T03-04's POST_ITEM),
#: POST_ITEM was bc4f92ac....
PRE_ITEM = {0: "8b5e882b0a4d771d56e8472ef557f84f",
            1: "e9aad997765ecb589711613cfb194444",
            2: "1139c7dcac2b0dd2b2ff6cbacc27e55c"}
POST_ITEM = {0: "1c9939fc22035400981bcf6b99b9d6f9",
             1: "8fbb92ad369b065bb83f8680d779ae5b",
             2: "ec354d2a2a8c8f9ad5d23317921b5f08"}
#: At `none`, the schema alone: seeds 0 and 1 mark nobody, so they equal POST_ITEM; seed 2 marks one survivor.
CONTROL = {0: POST_ITEM[0], 1: POST_ITEM[1], 2: "73702f7cbebebf053109e7fff536cedc"}   # B10-12 pin commit (CR-24 + MB-07r): seed 2 was 64304e58...
BUILD_PRE, BUILD_POST = "7266f56bea4e3d75705f5e88eec1b2e1", "600d8b27147478e158553552cc1409a5"


def revert_cp_t03_07(monkeypatch):
    """The item OFF, in process: `body_mark_model` at its control (`none`) on the shared fixtures, and the field taken
    out of `Person`'s canonical encoding (`state/world.py::_OBJECT_HEADS`, the cached head every Person digest reads),
    so a world hashes as it did before the field existed. Other tests that pin a pre-item hash call it."""
    monkeypatch.setitem(DEFAULT_FIXTURES._v, "body_mark_model", "none")
    names = tuple(f.name for f in fields(Person) if f.name != CEILING)
    monkeypatch.setitem(W._OBJECT_HEADS, Person,
                        (b"o" + W._str_bytes(Person.__name__) + b"%d:" % len(names),
                         tuple((n, W._str_bytes(n)) for n in names)))


def _floors():
    return DEFAULT_FIXTURES.get("band_floors")["body"].values()


def _fight(w, subject_state, actor_state=None, aid="cp307"):
    """`ACTOR` fights `SUBJECT` through the real fold and gate at RESOLVE, the band minted by `degree_of`."""
    d = SeasonDriver(w)
    w.step = Step.RESOLVE
    w.frozen = False
    raw = {"wound_state": {SUBJECT: subject_state, ACTOR: actor_state or party_state()}}
    res = Resolution(degree_of(raw, SUBJECT, w.fixtures), raw)
    out = d._fold(w, mint_token(w, WriteClass.ACTS), Act(id=aid, actor=ACTOR, verb="fight",
                                                         payload={"subject": SUBJECT}), res)
    w.log.extend(out)
    return res, out


DEEPEST = dict(wounds=3, max_wounds=3, full=10, left=4)     # standing, at the deepest gate: body 1000 -> 400
SHALLOW = dict(wounds=2, max_wounds=3, full=10, left=4)     # standing, one gate short of it


# ---- (i) the field, the row, the cells --------------------------------------------------------------------------

def test_the_field_is_built_at_condition_scale_and_has_one_row_and_three_writers():
    assert Person("x", "X").body_ceiling == DEFAULT_FIXTURES.get("condition_scale")
    row = MATRIX[("Person", CEILING)]
    assert Step.ENCOUNTER in row.steps and Step.RESOLVE in row.steps and not row.unproduced
    writers = sorted(v for v, r in VERB_TABLE.items() if f"Person.{CEILING}" in r.writes)
    assert writers == ["accept", "capture", "fight"]
    assert set(BODY_MARK_MODELS) == {"none", "deepest_gate"}
    assert DEFAULT_FIXTURES.get("body_mark_model") == "deepest_gate", "the shipped arm (REM-52's precedent)"


def test_marked_ceiling_walks_the_body_floors_and_stops_below_the_last():
    seen, c = [], DEFAULT_FIXTURES.get("condition_scale")
    for _ in range(len(list(_floors())) + 2):
        c = EC.marked_ceiling(c, _floors())
        seen.append(c)
    assert seen == [799, 499, 99, 99, 99]


# ---- (ii) the mark, written by the fight ------------------------------------------------------------------------

def test_a_survivor_at_the_deepest_gate_holds_799_and_a_shallower_one_is_unmarked():
    w = P.tiny_world()
    res, out = _fight(w, party_state(**DEEPEST))
    assert res.degree == WOUNDED and SUBJECT in w.persons
    p = w.persons[SUBJECT]
    assert (p.body_ceiling, p.body) == (799, 400)
    assert "body.changed" in [e.kind for e in out]
    assert w.persons[ACTOR].body_ceiling == DEFAULT_FIXTURES.get("condition_scale"), "the untouched party is unmarked"
    w2 = P.tiny_world()
    _fight(w2, party_state(**SHALLOW))
    assert (w2.persons[SUBJECT].body_ceiling, w2.persons[SUBJECT].body) == (1000, 400)


def _held_under_ceiling():
    """The 900-body fight held under 799: `(ceiling, body, [v of every (SUBJECT, "body", v) on body.changed])`."""
    w = P.tiny_world()
    _, out = _fight(w, party_state(wounds=3, max_wounds=3, full=10, left=9))     # 1000 * 9 // 10 = 900, above 799
    p = w.persons[SUBJECT]
    seen = [o.value for e in out if e.kind == "body.changed"
            for o in e.observed if (o.subject, o.predicate) == (SUBJECT, "body")]
    return p.body_ceiling, p.body, seen


def test_the_written_body_is_held_under_the_ceiling_and_the_observation_reports_it():
    assert _held_under_ceiling() == (799, 799, [799])


def test_mutation_an_observation_built_off_the_pre_clamp_body_reports_900_and_goes_red(monkeypatch):
    """The mutation, executed: the Observation is built from the body BEFORE the ceiling's `min` (the `_harm` value,
    900), the write still clamped. The assertion above then observes 900 where 799 was written."""
    real = EC.body_observed

    def pre_clamp(pid, body):
        return real(pid, 900 if (pid, body) == (SUBJECT, 799) else body)
    monkeypatch.setattr(EC, "body_observed", pre_clamp)
    got = _held_under_ceiling()
    assert got == (799, 799, [900]) != (799, 799, [799]), got


def test_a_felled_party_is_not_marked_and_the_marks_stop_at_the_last_floor():
    w = P.tiny_world()
    _fight(w, party_state(felled=True, wounds=4, max_wounds=3, full=10, left=0))
    assert SUBJECT not in w.persons
    w = P.tiny_world()
    for n, want in enumerate((799, 499, 99, 99)):
        _fight(w, party_state(**DEEPEST), aid=f"cp307-{n}")
        assert w.persons[SUBJECT].body_ceiling == want


def test_control_none_marks_nobody():
    w = P.tiny_world(DEFAULT_FIXTURES.sweep("body_mark_model", "none"))
    _fight(w, party_state(**DEEPEST))
    assert (w.persons[SUBJECT].body_ceiling, w.persons[SUBJECT].body) == (1000, 400)


def test_an_unregistered_model_refuses():
    w = P.tiny_world(DEFAULT_FIXTURES.sweep("body_mark_model", "no_such_model"))
    with pytest.raises(Exception, match="body-mark model"):
        EC._marks(w, {SUBJECT: 400}, {SUBJECT: party_state(**DEEPEST)})


# ---- (iii) the raiser heals toward the ceiling, and the falsifier -----------------------------------------------

def _tended(ceiling, body=250):
    """`tend` (computed, through the real resolve) on `SUBJECT` at `body`, his ceiling `ceiling`."""
    w, d = _world()
    p = w.persons["p_mid"]
    p.body_ceiling, p.body = ceiling, body
    (act,) = _tend_acts(w)
    _resolve(w, d, act)
    return w.persons["p_mid"]


def _falsifier_failures() -> list:
    bad = []
    marked, whole = _tended(799), _tended(DEFAULT_FIXTURES.get("condition_scale"))
    if marked.body != 799:
        bad.append(f"the marked man was tended to {marked.body}, not his ceiling 799")
    if whole.body != 1000:
        bad.append(f"the unmarked man was tended to {whole.body}, not 1000")
    if body_band_penalty(marked, DEFAULT_FIXTURES) != 1 or body_band_penalty(whole, DEFAULT_FIXTURES) != 0:
        bad.append("the marked man's budget does not sit one below whole")
    return bad


def test_falsifier_tend_heals_a_marked_man_to_799_and_an_unmarked_one_to_1000():
    assert _falsifier_failures() == []


def test_mutation_a_raiser_reading_condition_scale_lifts_him_past_799_and_the_falsifier_goes_red(monkeypatch):
    real = EFFECTS["tend"]

    def mutant(w, a, res=None):
        change = real(w, a, res)
        who = w.persons[a.payload["subject"]]

        def perform():
            who.body = max(who.body, int(w.fixtures.get("condition_scale")))
        return type(change)(change.subjects, perform, change.ending)
    monkeypatch.setitem(EFFECTS, "tend", mutant)
    bad = _falsifier_failures()
    assert bad and "not his ceiling 799" in bad[0], bad


def test_a_fight_then_tend_end_to_end():
    w, d = _world()
    _fight(w, party_state(**DEEPEST))
    w.persons[SUBJECT].body = 250
    (act,) = _tend_acts(w)
    _resolve(w, d, act)
    assert w.persons[SUBJECT].body == 799


# ---- the asymmetry guard (CLAUDE.md §0.1 pt 1) ------------------------------------------------------------------

_SEASON = pathlib.Path(EC.__file__).resolve().parents[1]

#: Every bare write of `body` in the season package outside `tests/` and `harness/`, by its stripped text, with how
#: it stands to the ceiling. `lowers`: it never raises a body (a fall, a wound, a death), so the ceiling cannot bind
#: it. `raises`: it raises a body, and its function must heal to `body_ceiling` (checked below). Anything else fails.
_BODY_WRITES = {
    # `_eff_kill`'s `_wound`: the body `_harm` left, already held under the mark's ceiling (`_marks`).
    "w.persons[pid].body = body": "lowers",
    # `_eff_march`: the losing side's casualties, `total` and `scaled_by_degree` arms.
    "p.body = 0": "lowers",
    # (B10-12 pin commit: CP-T04-01 changed `pct` to `mine`, the loser's own subunit ratio under `field_subunits: person`.)
    "p.body = max(1, int(p.body * max(0.0, mine or 0.0)))": "lowers",
    # `_eff_march` (CR-24, `field_winner_casualties: engine`): the winners' own casualties, `body` only; `win_ratio` is clamped
    # to [0, 1] at its one write (`min(1.0, max(0.0, mine))`), so the write can only hold or lower a body.
    'p.body = 0 if model == "total" else max(1, int(p.body * win_ratio[pid]))': "lowers",
    # `_eff_tend`: the one raiser at HEAD; `whole` is `max(p.body, p.body_ceiling)`.
    "p.body = whole": "raises",
    # `loop/matter.py`'s subsistence fall (`fall.body_after`, a loss), in the `setattr` form a `.body =` grep misses.
    'lambda person=person, after=fall.body_after: setattr(person, "body", after),': "lowers",
}

_ASSIGN = re.compile(r'^\s*(?:if [^:]+:\s*)?(?:[^;#]*;\s*)*([A-Za-z_][\w.\[\]]*\.body\s*(?:=|-=|\+=)[^=].*?)\s*(?:#.*)?$')
_SETATTR = re.compile(r'setattr\([^,]+,\s*["\']body["\']')


def _scan(text: str) -> list:
    out = []
    for n, line in enumerate(text.splitlines(), 1):
        if line.lstrip().startswith("#"):
            continue
        m = _ASSIGN.match(line)
        if m:
            out.append((n, m.group(1).strip()))
        elif _SETATTR.search(line):
            out.append((n, line.strip()))
    return out


def _season_sources():
    for f in sorted(_SEASON.rglob("*.py")):
        rel = f.relative_to(_SEASON).parts
        if rel[0] in ("tests", "harness"):
            continue
        yield f


def _check_source(text: str, rel: str, found: list, offenders: list) -> int:
    """One source through the guard: appends every scanned write to `found` and every unregistered write or unbounded
    raiser to `offenders`; returns how many registered raisers it checked."""
    tree, raisers = None, 0
    for n, line in _scan(text):
        found.append(line)
        role = _BODY_WRITES.get(line)
        if role is None:
            offenders.append(f"{rel}:{n}: {line}")
            continue
        if role == "raises":
            raisers += 1
            tree = tree or ast.parse(text)
            # the MODULE-LEVEL function holding the write (the effect, not its `perform` closure)
            fn = next(node for node in tree.body
                      if isinstance(node, ast.FunctionDef) and node.lineno <= n <= node.end_lineno)
            nodes = list(ast.walk(fn))
            if not any(isinstance(x, ast.Attribute) and x.attr == CEILING for x in nodes):
                offenders.append(f"{rel}:{n}: raiser `{fn.name}` does not read {CEILING}")
            if any(isinstance(x, ast.Constant) and x.value == "condition_scale" for x in nodes):
                offenders.append(f"{rel}:{n}: raiser `{fn.name}` reads condition_scale")
    return raisers


def test_every_bare_body_write_is_registered_and_every_raiser_heals_to_the_ceiling():
    found, offenders, raisers = [], [], 0
    for f in _season_sources():
        raisers += _check_source(f.read_text(encoding="utf-8"), str(f.relative_to(_SEASON)), found, offenders)
    assert raisers >= 1 and len(found) >= len(_BODY_WRITES), (found, "the guard observed nothing")
    assert sorted(set(found)) == sorted(_BODY_WRITES), ("a registered write is gone; delete its entry", found)
    assert not offenders, ("an unregistered or unbounded `body` write -- register it in _BODY_WRITES with its role, "
                           "and a raiser heals to `body_ceiling`:\n  " + "\n  ".join(offenders))


def test_the_guard_itself_can_fail():
    planted = ("    x = 1; who.body = who.body + 5\n"
               "    w.write('b', t, lambda q=q: setattr(q, 'body', 9))\n")
    got = [line for _, line in _scan(planted)]
    assert len(got) == 2 and all(line not in _BODY_WRITES for line in got)


_PLANTED_RAISERS = {
    # a registered raiser that reads `condition_scale` (and the ceiling): the second AST branch
    "reads condition_scale": ("def _eff_tend(w, a, res=None):\n"
                              "    p = w.persons[a.payload['subject']]\n"
                              "    whole = max(p.body, p.body_ceiling, w.fixtures.get('condition_scale'))\n"
                              "    def perform():\n"
                              "        p.body = whole\n"
                              "    return perform\n"),
    # a registered raiser that never reads `body_ceiling`: the first AST branch
    "does not read body_ceiling": ("def _eff_tend(w, a, res=None):\n"
                                   "    p = w.persons[a.payload['subject']]\n"
                                   "    whole = max(p.body, 1000)\n"
                                   "    def perform():\n"
                                   "        p.body = whole\n"
                                   "    return perform\n"),
}


@pytest.mark.parametrize("why", sorted(_PLANTED_RAISERS))
def test_the_raiser_branch_of_the_guard_can_fail(why):
    found, offenders = [], []
    raisers = _check_source(_PLANTED_RAISERS[why], "planted.py", found, offenders)
    assert raisers == 1 and found == ["p.body = whole"], (raisers, found)
    assert len(offenders) == 1 and offenders[0].endswith(why) and "`_eff_tend`" in offenders[0], offenders


# ---- hashes: the declared mover and its control ------------------------------------------------------------------

@pytest.mark.parametrize("seed", [0, 1, 2])
def test_hash_post_item_control_and_revert(seed, monkeypatch):
    # v11 CP-T03-08 (`tend` forms on the wounded, a later formation mover of every season) is reverted in process, so
    # POST_ITEM still reads this item alone (imported here: that module imports this one).
    from .test_cp_t03_08_tend_on_the_wounded import revert_cp_t03_08
    revert_cp_t03_08(monkeypatch)
    # CR-79's credit term (a later mover of the told deposit) is reverted in process too.
    from .test_strife_credit import revert_cr79
    revert_cr79(monkeypatch)
    w = build_realm(seed)
    run(1, seed, w=w)
    scale = w.fixtures.get("condition_scale")
    marked = sum(1 for p in w.persons.values() if p.body_ceiling < scale)
    assert w.content_hash() == POST_ITEM[seed] != PRE_ITEM[seed]
    assert marked == {0: 0, 1: 0, 2: 1}[seed], "persons carrying a mark after one season"
    monkeypatch.setitem(DEFAULT_FIXTURES._v, "body_mark_model", "none")
    w = build_realm(seed)
    run(1, seed, w=w)
    assert w.content_hash() == CONTROL[seed]
    revert_cp_t03_07(monkeypatch)
    w = build_realm(seed)
    run(1, seed, w=w)
    assert w.content_hash() == PRE_ITEM[seed]


def test_build_hash_is_a_schema_mover_and_the_revert_reads_the_old_one(monkeypatch):
    assert build_realm(0).content_hash() == BUILD_POST
    revert_cp_t03_07(monkeypatch)
    assert build_realm(0).content_hash() == BUILD_PRE
