"""G2 -- one `Token`, minted in `loop/driver` only. Plan position 5.

`04:199` -- *"`Token := (write_class, tick)` -- constructed by loop/driver and NOWHERE ELSE"*.
`04:206` -- *"only the driver mints a Token | MECHANICAL -- a test asserts `Token(` appears in
`loop/driver` only | MECHANICAL, same scan; GDScript has no private constructors"*. This file is
the Python half of that row; the GDScript half is out of scope before the port (position 26).

Four claims, each with the control that stops it passing vacuously:

  1. THE SCAN. No `Token(` outside `loop/driver.py`, and no `mint_token(` from game code outside
     it -- over a counted, named set of files, with planted violations it must find and the
     driver's own construction it must see.
  2. THE GATE. A write with no token fails AS `NoToken` -- not for want of a matrix row -- and a
     token from another tick fails the same way.
  3. THE FOLD. The S30.2 class check on the fold's own writes is no longer circular: a fold handed
     the wrong token is refused.
  4. DELIBERATE MUTATES NO STORE BY ANY ROUTE -- measured on the `World` itself around every
     DELIBERATE call, not inferred from which functions it calls. This is the assertion that would
     have caught `w._rehome()` (`ED-IN-0206`), including the route through the `w.tenures` getter.
"""
import ast
import enum
import functools
import pathlib
import types

import pytest

from engine.season.data.matrix import Step, WriteClass
from engine.season.decision import make_chooser
from engine.season.gaps import Forbidden, InstrumentDefect, ShapeGap, Unspecified
from engine.season.harness import headless as HL
from engine.season.harness import probes as P
from engine.season.loop.driver import SeasonDriver, mint_token, resolvable_verbs
from engine.season.state.carriers import Act, StateChange, Tenure
from engine.season.state.gate import NoToken, Token
from engine.season.state.ids import H, draw_factory

SEASON = pathlib.Path(__file__).resolve().parents[1]          # engine/season
DRIVER = "loop/driver.py"
# Apparatus stands in for the driver at a synthetic barrier and may CALL the driver's minter; it
# may not CONSTRUCT a token. Everything else under `engine/season/` is game code and may do neither.
APPARATUS = ("harness/", "tests/")
# The seven steps (six until M4 added `encounter.py`, `ED-IN-0279` clause (a)), named, so the
# floor is on WHICH files the scan read and not only how many.
STEP_MODULES = {f"loop/{s}.py" for s in
                ("calendar", "matter", "deliberate", "resolve", "encounter", "witness", "census")}


# ======================================================================================
# 1 -- THE SCAN
# ======================================================================================

def _callee(call: ast.Call):
    f = call.func
    return f.id if isinstance(f, ast.Name) else f.attr if isinstance(f, ast.Attribute) else None


def _token_scan(sources: dict) -> tuple:
    """`(violations, constructions)` over `{relative path: source}`.

    ⚠ WHAT IT CANNOT SEE, NAMED RATHER THAN IMPLIED AWAY: `type(t)(...)`, `dataclasses.replace(t,
    ...)` and `copy.copy(t)` each produce a token without spelling `Token(`. Rebinding the name is
    NOT in that list -- `X = Token` and `import ... Token as X` are both flagged below, because each
    is the one-line way to make every later construction invisible to this scan."""
    bad, constructions = [], []
    for rel, src in sorted(sources.items()):
        apparatus = rel.startswith(APPARATUS)
        for n in ast.walk(ast.parse(src, rel)):
            if isinstance(n, ast.Call):
                name = _callee(n)
                if name == "Token":
                    constructions.append(f"{rel}:{n.lineno}")
                    if rel != DRIVER:
                        bad.append(f"{rel}:{n.lineno} constructs a Token outside the driver")
                elif name == "mint_token" and rel != DRIVER and not apparatus:
                    bad.append(f"{rel}:{n.lineno} calls mint_token from game code -- a step is "
                               f"HANDED its token, it does not mint one")
            elif isinstance(n, (ast.Import, ast.ImportFrom)):
                for a in n.names:
                    if a.name in ("Token", "mint_token") and a.asname and rel != DRIVER:
                        bad.append(f"{rel}:{n.lineno} imports {a.name} as {a.asname!r}")
            elif isinstance(n, (ast.Assign, ast.AnnAssign)) and rel != DRIVER:
                v = n.value
                if isinstance(v, ast.Name) and v.id in ("Token", "mint_token"):
                    bad.append(f"{rel}:{n.lineno} rebinds {v.id}")
    return bad, constructions


def _tree_sources() -> dict:
    return {str(f.relative_to(SEASON)): f.read_text()
            for f in sorted(SEASON.rglob("*.py")) if "__pycache__" not in f.parts}


def test_g2_token_is_constructed_in_loop_driver_only():
    """`04:206`'s MECHANICAL grade, run over the whole of `engine/season/` INCLUDING `tests/` and
    `harness/` (which may call `mint_token` but may not construct)."""
    src = _tree_sources()
    bad, constructions = _token_scan(src)
    assert not bad, "\n".join(bad)
    # THE FLOOR, ON COUNT AND ON IDENTITY. A scan rooted at the wrong directory reads nothing and
    # passes; this is what makes that red. 69 files at the time of writing.
    assert len(src) >= 60, f"the scan read {len(src)} files -- is it rooted at engine/season?"
    missing = STEP_MODULES - set(src)
    assert not missing, f"the scan did not read the step modules {sorted(missing)}"
    # THE POSITIVE CONTROL: the scan must SEE the one construction there is. If this finds zero,
    # the scanner cannot recognise a construction and the empty `bad` above means nothing.
    assert [c.split(":")[0] for c in constructions] == [DRIVER], constructions


def test_g2_the_scan_reddens_on_a_planted_construction_in_deliberate():
    """THE PLAN'S FIRST FALSIFIER, KEPT RUNNING. A `Token(` planted in `loop/deliberate.py` must be
    found; so must a `mint_token(` call and an aliasing import there. The same `Token(` planted in
    the DRIVER must NOT be -- otherwise the scan flags every construction and proves nothing."""
    src = _tree_sources()
    delib = src["loop/deliberate.py"]
    anchor = "    w.step = Step.DELIBERATE\n"
    assert delib.count(anchor) == 1, "the plant's anchor moved; re-point it"
    plants = {
        "construct": "    _t = Token(WriteClass.ACTS, w.tick)\n",
        "mint": "    _t = mint_token(w, WriteClass.ACTS)\n",
        "alias": "    from ..state.gate import Token as _T\n",
        "rebind": "    _T = Token\n",
    }
    for label, line in plants.items():
        planted = dict(src, **{"loop/deliberate.py": delib.replace(anchor, anchor + line)})
        bad, _ = _token_scan(planted)
        assert any(b.startswith("loop/deliberate.py:") for b in bad), (
            f"the scan did not see a planted {label} in DELIBERATE: {line.strip()!r}")
    driver = src[DRIVER]
    planted = dict(src, **{DRIVER: driver + "\n_extra = Token(WriteClass.ACTS, 0)\n"})
    bad, constructions = _token_scan(planted)
    assert not bad and len(constructions) == 2, (bad, constructions)


def test_g2_season_hands_six_steps_a_token_and_deliberate_none():
    """`04 §C.1`, read off the driver's own `season()`: six barrier calls each receive a
    `mint_token(...)` as their first argument, in the class §C.1 names (`encounter` shares
    RESOLVE's `WriteClass.ACTS`, M4, `ED-IN-0279` clause (a)), and `deliberate` receives no
    `mint_token` at all."""
    tree = ast.parse(_tree_sources()[DRIVER])
    season = next(n for n in ast.walk(tree)
                  if isinstance(n, ast.FunctionDef) and n.name == "season")
    handed = {}
    for n in ast.walk(season):
        if (isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
                and isinstance(n.func.value, ast.Name) and n.func.value.id == "self"):
            first = n.args[0] if n.args else None
            if isinstance(first, ast.Call) and _callee(first) == "mint_token":
                handed[n.func.attr] = ast.unparse(first.args[1])
            elif n.func.attr == "deliberate":
                assert not any(_callee(a) == "mint_token" for a in ast.walk(n)
                               if isinstance(a, ast.Call)), "DELIBERATE was handed a token"
                handed["deliberate"] = None
    assert handed == {
        "calendar": "WriteClass.CALENDAR", "matter": "WriteClass.MATTER",
        "deliberate": None, "resolve": "WriteClass.ACTS",
        "encounter": "WriteClass.ACTS",
        "witness": "WriteClass.INTERIOR", "census": "WriteClass.MATTER",
    }, handed


# ======================================================================================
# 2 -- THE GATE
# ======================================================================================

def _write_stores(w, credential, applied: list):
    """The plan's WRAPPER: a gate write on a row that is ADMITTED at RESOLVE in the ACTS class
    (`(Rung, stores)`, the same row `test_w3_the_write_class_check_still_refuses_a_wrong_class`
    admits), so the only thing that can make it fail is the credential."""
    return w.write("stores", credential, lambda: applied.append(1),
                   record_kind="Rung", fieldname="stores", driver="Act")


def test_g2_a_gate_write_without_a_token_fails_for_want_of_a_token():
    """THE PLAN'S SECOND FALSIFIER. Assert on WHICH error, not that one was raised."""
    w = P.tiny_world()
    w.step = Step.RESOLVE
    applied: list = []
    # THE CONTROL FIRST: with a token this exact write is admitted, so the row, the step and the
    # class are all lawful and nothing but the credential below can refuse it.
    _write_stores(w, mint_token(w, WriteClass.ACTS), applied)
    assert applied == [1], "the control write did not apply; the wrapper is not a lawful write"
    # The pre-G2 call shape -- a bare `WriteClass` -- and no credential at all.
    for bare in (WriteClass.ACTS, None, "ACTS"):
        with pytest.raises(NoToken) as e:
            _write_stores(w, bare, applied)
        assert type(e.value) is NoToken and "not a Token" in str(e.value), str(e.value)
        assert isinstance(e.value, InstrumentDefect) and not isinstance(e.value, ShapeGap), (
            "a missing token must file as a call-site bug, never as a hole in the design")
    assert applied == [1], "a refused write still ran its `apply()`"
    # THE ORDER: an ABSENT matrix row with no token is refused for the TOKEN -- the check runs
    # first -- and the same absent row WITH a token is refused for the ROW. Both halves, so the
    # first is not simply what any bad write raises.
    with pytest.raises(NoToken):
        w.write("nope", WriteClass.ACTS, lambda: None,
                record_kind="NoSuchKind", fieldname="nope", driver="Act")
    with pytest.raises(Unspecified):
        w.write("nope", mint_token(w, WriteClass.ACTS), lambda: None,
                record_kind="NoSuchKind", fieldname="nope", driver="Act")


def test_g2_a_token_from_another_tick_is_refused():
    """The tick is READ: a token kept past its barrier authorizes nothing a season later."""
    w = P.tiny_world()
    w.step = Step.RESOLVE
    stale = mint_token(w, WriteClass.ACTS)
    w.tick += 1
    applied: list = []
    with pytest.raises(NoToken) as e:
        _write_stores(w, stale, applied)
    assert f"tick {stale.tick}" in str(e.value) and applied == [], str(e.value)
    _write_stores(w, mint_token(w, WriteClass.ACTS), applied)            # control: fresh token
    assert applied == [1]


def test_g2_a_token_cannot_be_rewritten_in_place():
    """`frozen=True` is the one STRUCTURAL part: a MATTER token cannot become an ACTS token."""
    t = mint_token(P.tiny_world(), WriteClass.MATTER)
    assert isinstance(t, Token)
    with pytest.raises(AttributeError):
        t.write_class = WriteClass.ACTS
    assert t.write_class is WriteClass.MATTER


# ======================================================================================
# 3 -- THE FOLD
# ======================================================================================

def test_g2_the_fold_is_no_longer_circular_a_wrong_token_is_refused():
    """`_apply_write` passed `mrow.write_class(Step.RESOLVE)`, which `World.write` recomputed
    from the same map -- so S30.2 could not fail for any fold write. It passes the driver's token
    now; hand the fold a MATTER token at RESOLVE and the gate must refuse it on the CLASS."""
    w = P.tiny_world()
    d = SeasonDriver(w)
    w.step = Step.RESOLVE
    # ⚠ G4: THE ACT NOW DECLARES A DELTA. It declared none, and the control arm below asserted
    # `site.worked` for a `work` that repaired nothing -- `H-94`'s worked case, which G4's
    # `NoOpReceipt` refuses (`work.unavailable`). The control must be an act that DOES the thing,
    # or it is not a control; a delta of 1 is the smallest that is one. The wrong-token arm is
    # unaffected: the class is refused before anything is staged.
    act = lambda aid: Act(id=aid, actor="p_low", verb="work", payload={"site": "site_harbour"},
                          changes=[StateChange("site_harbour", "alter", "Act", "condition", 1)])
    with pytest.raises(Forbidden) as e:
        d._fold(w, mint_token(w, WriteClass.MATTER), act("g2_wrong"))
    assert e.value.where == "S30.2" and "class" in str(e.value), (e.value.where, str(e.value))
    # control: the same act with the ACTS token is admitted and does the thing.
    ok = [ev.kind for ev in d._fold(w, mint_token(w, WriteClass.ACTS), act("g2_right"))]
    assert ok == ["site.worked"], ok


# ======================================================================================
# 4 -- DELIBERATE MUTATES NO STORE, BY ANY ROUTE
# ======================================================================================

# Attributes of `World` that are NOT stores, each with the reason. Everything else in `vars(w)`
# -- including any attribute added after this was written -- is digested, so a new store is
# covered by default rather than by someone remembering to list it.
_NOT_STORES = {
    "step": "barrier bookkeeping: which step is running. DELIBERATE sets it on entry",
    "_in_parallel_map": "barrier bookkeeping: S51's flag, set and cleared inside DELIBERATE",
}


def _deep(o, seen: tuple = ()) -> str:
    if isinstance(o, (str, int, float, bool, type(None), enum.Enum)):
        return repr(o)
    if isinstance(o, (types.FunctionType, types.MethodType, types.BuiltinFunctionType,
                      functools.partial, type)):
        return f"<{type(o).__name__}>"
    if id(o) in seen:
        return "<cycle>"
    seen = seen + (id(o),)
    if isinstance(o, dict):
        return "{" + ",".join(sorted(f"{_deep(k, seen)}:{_deep(v, seen)}"
                                     for k, v in o.items())) + "}"
    if isinstance(o, (list, tuple)):
        return "[" + ",".join(_deep(x, seen) for x in o) + "]"
    if isinstance(o, (set, frozenset)):
        return "{" + ",".join(sorted(_deep(x, seen) for x in o)) + "}"
    attrs = dict(getattr(o, "__dict__", {}))
    for cls in type(o).__mro__:
        for s in getattr(cls, "__slots__", ()):
            if hasattr(o, s):
                attrs[s] = getattr(o, s)
    return type(o).__name__ + _deep(attrs, seen)


def _store_digest(w) -> dict:
    """Every `World` attribute except `_NOT_STORES`, digested by CONTENT. `fixtures` is digested by
    its VALUES: its `reads` counter is read-tracking every `fixtures.get` bumps, and counting it
    would call a read a write. Reads `vars(w)` directly -- never the `tenures` getter, which is
    one of the routes under test."""
    out = {}
    for k, v in vars(w).items():
        if k in _NOT_STORES:
            continue
        out[k] = _deep(v._v if k == "fixtures" else v)
    return out


def _chooser(w):
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    return make_chooser(w.fixtures, mint, verbs=resolvable_verbs(),
                        draw=draw_factory(w.world_seed, lambda: w.tick))


def test_g2_deliberate_mutates_no_store_by_any_route(monkeypatch):
    """`04 §A.2`: DELIBERATE *"owns nothing ... token: none"*. Checked on the WORLD around every
    DELIBERATE call, so it sees a mutation whatever function makes it -- `gate.write`, a direct
    assignment, a store method, or a read with a side effect such as the `w.tenures` getter's old
    `_rehome()`.

    TWO ARMS, BECAUSE ONE CANNOT SEE `_rehome`. The SEASON arm runs real seasons; but MATTER now
    homes every Tenure before the freeze, so `_rehome` is a no-op by the time DELIBERATE runs and
    restoring the old call would leave that arm green. The PLANTED arm calls DELIBERATE directly on
    a world holding an unhomed Tenure, which is the one state in which the old call MUTATES --
    so it is the arm that reddens. MUTATION (run 2026-09-26): restore `w._rehome()` at the head of
    `deliberate`, or `self._rehome()` in the `World.tenures` getter, and the planted arm goes RED;
    unmutated it is GREEN."""
    real = SeasonDriver.deliberate
    checked = {"calls": 0, "acts": 0}

    def spy(self, *a, **k):
        before = _store_digest(self.w)
        acts = real(self, *a, **k)
        after = _store_digest(self.w)
        moved = sorted(key for key in set(before) | set(after) if before.get(key) != after.get(key))
        assert not moved, f"DELIBERATE mutated World.{moved} at tick {self.w.tick}"
        checked["calls"] += 1
        checked["acts"] += len(acts)
        return acts

    monkeypatch.setattr(SeasonDriver, "deliberate", spy)

    # -- the SEASON arm ----------------------------------------------------------------
    for w in (P.tiny_world(), HL.build_world(0)):
        d, ch = SeasonDriver(w), _chooser(w)
        for _ in range(2):
            d.season(ch, question=None, subsistence=P.SUBSIST,
                     contest_max_depth=w.fixtures.get("contest_max_depth"))
    # THE FLOOR: two worlds x two seasons x `scene_budget` rounds, and DELIBERATE must have
    # returned acts -- a map that returned nothing proves nothing about a map that decides.
    # MEASURED 2026-09-26: 20 calls, 67 acts. The floor is set for non-vacuity, not at the
    # measurement, so a `scene_budget` sweep does not redden a test about something else.
    assert checked["calls"] >= 8 and checked["acts"] >= 30, checked
    season_calls = checked["calls"]

    # -- the PLANTED arm ---------------------------------------------------------------
    w = P.tiny_world()
    p = w.persons.pop("p_low")
    w.add_tenure(Tenure("t_g2_orphan", "p_low", "p_mid", "tie", since=0))  # subject first...
    w.persons["p_low"] = p                                                 # ...person second
    assert [t.id for t in w._unowned if t.subject in w.persons] == ["t_g2_orphan"], (
        "the plant did not leave an unhomed Tenure; the route is not being exercised")
    w.frozen = True
    d2 = SeasonDriver(w)
    # ⚠ MERGE, 2026-09-27 (ED-IN-0206, main): `deliberate` now takes `questions` as its fourth
    # positional argument -- the per-person projection the driver builds at barrier 2 and used to
    # compute inside `deliberate` itself. Built the same way `season()` builds it, so the planted
    # call exercises the real shape rather than an empty stand-in.
    d2.deliberate(_chooser(w), None, P.SUBSIST, d2._questions_at_barrier())   # the spy asserts no store moved
    assert "t_g2_orphan" in [t.id for t in w._unowned], "DELIBERATE homed the Tenure"
    assert checked["calls"] == season_calls + 1, "the planted call did not pass through the spy"

    # -- the digest can SEE this mutation (§0.1 pt 2) ------------------------------------
    # Without this the planted arm's green could be a digest that ignores tenure layout.
    before = _store_digest(w)
    w._rehome()
    after = _store_digest(w)
    assert before != after and "t_g2_orphan" in [t.id for t in p.tenures], (
        "the digest did not change when the tenure store did -- it cannot observe the failure "
        "this test exists to exclude")
