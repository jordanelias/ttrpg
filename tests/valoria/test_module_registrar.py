"""THE REGISTRAR AND THE DRIVER-CONSTRUCTION REFUSALS -- plan position `30` (A-25; `ED-IN-0284`,
revised by `ED-IN-0285`). One planted violation per refusal, EACH IN A FRESH SUBPROCESS.

WHY A SUBPROCESS PER CASE. `MODULE_ENTRIES` (`engine/season/manifest/registrar.py`), `PROVIDERS`
(`manifest/providers.py`) and `EFFECTS` (`loop/effects_shared.py`) are process globals: inside a
pytest process another test's imports can fill them, so an in-process test can pass on a table it
did not build. `tests/valoria/test_season_providers_are_registered.py` is the precedent.

SUBJECT, under `CLAUDE.md` §0.1 pt 5: these are the loader's refusals per data family
(`CLAUDE.md` §0.05, "the loader's refusal per data family") over rows the game resolves from -- the
composition rows, the prize rows and the verb rows -- and each refusal replaces a path by which a
verb used to leave the game without a word. Load-bearing on the game.

`ID-13`, READ EXACTLY: no production composition row carries `entry:` at `30`, so every registrar
case below PLANTS one; the registrar's pass over production rows is first exercised at `31a`.

The plan's falsifiers, by number (`workplans/valoria_master_workplan_v8_part5.md`, position `30`):
(2) `test_a_registered_row_deleted_under_a_live_process_refuses_naming_it` and
`test_a_verb_call_row_naming_no_verb_refuses_naming_it`; (3) `test_a_prize_row_with_its_provider_cleared_refuses_naming_the_prize`;
(4) `test_a_verb_contesting_a_prize_no_row_claims_refuses_naming_the_verb`; (5)
`test_a_writing_row_with_its_effect_cleared_refuses_naming_the_verb`; (6) the three
`test_one_entry_registered_twice_*`; (7) `test_the_populated_realm_constructs_a_driver_and_every_check_ran`;
(8) `test_the_composition_export_round_trips`, with
`test_engine_does_not_import_systems.py::test_importing_every_engine_module_pulls_in_no_subsystem`.
"""
from __future__ import annotations

import os
import subprocess
import sys

ROOT = __file__.rsplit("/tests/", 1)[0]

_HEAD = """
import sys
sys.path.insert(0, {root!r})
from engine.substrate import composition
from engine.season.loop.driver import SeasonDriver, EFFECTS, VERB_TABLE
from engine.season.state.world import World
from engine.season.manifest import MODULE_ENTRIES

def construct():
    try:
        SeasonDriver(World(0))
        return None
    except Exception as exc:                  # the type is asserted by the test
        return (type(exc).__name__, str(exc))

# A real engine-side callable, so a planted row resolves by string without naming any module code.
TARGET = "engine.dice_engine.dice_engine:degree_from_net"
def plant(role, verb, target=TARGET, entry="verb_call"):
    composition.ROLES[role] = dict(target=target, kind="callable", entry=entry, verb=verb,
                                   needed_by="planted by tests/valoria/test_module_registrar.py")
"""


def _run(body: str):
    """Run `_HEAD` + `body` in a fresh interpreter; `body` prints one `repr(...)`, returned evaluated."""
    out = subprocess.run([sys.executable, "-c", _HEAD.format(root=ROOT) + body],
                         capture_output=True, text=True, timeout=600)
    assert out.returncode == 0, out.stderr[-3000:]
    return eval(out.stdout.strip().splitlines()[-1])     # our own probe's repr


def _assert_refused(refusal, *names):
    assert refusal is not None, f"driver construction did NOT refuse; expected it to name {names}"
    kind, text = refusal
    assert kind == "Unspecified", refusal
    for n in names:
        assert n in text, f"the refusal does not name {n!r}: {text}"


def test_a_planted_entry_is_registered_by_string_at_construction_and_idempotently():
    """The registrar's positive half: a row with `entry:` is in `MODULE_ENTRIES` after construction,
    resolved to the target's callable, and NOT before it (registration is at construction, never at
    import); constructing again refuses nothing and leaves the one table unchanged."""
    got = _run("""
verb = sorted(VERB_TABLE)[0]
plant("planted.entry", verb)
before = sorted(MODULE_ENTRIES)
first = construct()
after = {r: (e.entry, e.verb, e.target, e.fn.__name__) for r, e in MODULE_ENTRIES.items()}
second = construct()
again = {r: (e.entry, e.verb, e.target, e.fn.__name__) for r, e in MODULE_ENTRIES.items()}
print(repr((verb, before, first, after, second, again)))
""")
    verb, before, first, after, second, again = got
    assert before == [], f"MODULE_ENTRIES was filled before any driver was constructed: {before}"
    assert first is None and second is None, (first, second)
    assert after == {"planted.entry": ("verb_call", verb, "engine.dice_engine.dice_engine:degree_from_net",
                                       "degree_from_net")}, after
    assert again == after, "a second construction changed MODULE_ENTRIES -- the registrar is not idempotent"


def test_a_registered_row_deleted_under_a_live_process_refuses_naming_it():
    """Falsifier (2): delete a planted composition row -> driver construction refuses naming it.

    The table holds an entry no row declares: written by a second writer, or by a row since deleted.
    ⚠ This is the within-process form. In a FRESH process a deleted row leaves nothing behind to
    refuse on, because no data at `30` declares that a row must exist -- verb rows name no module
    (A-25) -- and the receipt says so."""
    refusal = _run("""
plant("planted.entry", sorted(VERB_TABLE)[0])
assert construct() is None
del composition.ROLES["planted.entry"]
print(repr(construct()))
""")
    _assert_refused(refusal, "planted.entry", "no composition row declares")


def test_a_verb_call_row_naming_no_verb_refuses_naming_it():
    """Refusal (b): an `entry: verb_call` row whose `verb:` names no verb row."""
    refusal = _run("""
plant("planted.orphan", "a verb nobody declared")
print(repr(construct()))
""")
    _assert_refused(refusal, "planted.orphan", "a verb nobody declared")


def test_one_entry_registered_twice_by_two_rows_with_one_target_refuses():
    """Falsifier (6), refusal (d): one module entry, two composition rows."""
    refusal = _run("""
verbs = sorted(VERB_TABLE)
plant("planted.one", verbs[0])
plant("planted.two", verbs[1])
print(repr(construct()))
""")
    _assert_refused(refusal, "registered twice", "planted.one", "planted.two")


def test_one_entry_registered_twice_by_two_verb_calls_for_one_verb_refuses():
    """Refusal (d): which module a verb calls has one answer -- two `verb_call` rows for one verb."""
    refusal = _run("""
verb = sorted(VERB_TABLE)[0]
plant("planted.one", verb)
plant("planted.two", verb, target="engine.dice_engine.dice_engine:degree_label")
print(repr(construct()))
""")
    _assert_refused(refusal, "planted.one", "planted.two")


def test_one_entry_registered_twice_by_a_second_writer_refuses():
    """Refusal (d): the table already holds the role, bound by something other than the registrar."""
    refusal = _run("""
from engine.season.manifest import ModuleEntry
verb = sorted(VERB_TABLE)[0]
plant("planted.entry", verb)
MODULE_ENTRIES["planted.entry"] = ModuleEntry("planted.entry", "verb_call", verb, TARGET, print)
print(repr(construct()))
""")
    _assert_refused(refusal, "planted.entry", "registered twice")


def test_a_prize_row_with_its_provider_cleared_refuses_naming_the_prize():
    """Falsifier (3), refusal (c) half 2: a prize row whose `provider:` nobody registered. The prize
    is chosen from the roster, not named here (no entity is special-cased)."""
    got = _run("""
import engine.season.manifest.registry as R
real = R.roster_map
prize = sorted(real("contest_subsystems", "prizes"))[0]
def cleared(roster, column):
    rows = real(roster, column)
    if (roster, column) == ("contest_subsystems", "prizes"):
        rows = dict(rows, **{prize: dict(rows[prize], provider=None)})
    return rows
R.roster_map = cleared
print(repr((prize, construct())))
""")
    prize, refusal = got
    _assert_refused(refusal, repr(prize), "nobody registered")


def test_a_verb_contesting_a_prize_no_row_claims_refuses_naming_the_verb():
    """Falsifier (4), refusal (c) half 1. The loader refuses this at load (`data/verbs.py`, invariant
    9), so it reaches the driver only through a table changed after load -- planted that way here."""
    got = _run("""
import dataclasses
verb = sorted(v for v, r in VERB_TABLE.items() if r.contests)[0]
VERB_TABLE[verb] = dataclasses.replace(VERB_TABLE[verb], contests="a prize nobody claims")
print(repr((verb, construct())))
""")
    verb, refusal = got
    _assert_refused(refusal, repr(verb), "a prize nobody claims")


def test_a_writing_row_with_its_effect_cleared_refuses_naming_the_verb():
    """Falsifier (5), refusal (a): clear the effect of a writing row that carries no `decline_note:`.
    Chosen from the tables -- a writing, uncontested row with an effect and no decline -- not named."""
    got = _run("""
from engine.season.manifest.registry import _declined_verbs
verb = sorted(v for v, r in VERB_TABLE.items()
              if r.writes and not r.contests and v in EFFECTS and v not in _declined_verbs())[0]
del EFFECTS[verb]
print(repr((verb, construct())))
""")
    verb, refusal = got
    _assert_refused(refusal, repr(verb), "decline_note")


def test_refusal_a_is_one_sided_and_exempts_contests():
    """Refusal (a)'s two declared limits, observed: a writing row with no effect that DOES carry a
    `decline_note:` constructs (every shipped such row does), and the converse arm -- a row carrying
    BOTH an effect and a `decline_note:` (`SM-9`) -- is NOT refused, since the column also declines
    a formation on some rows. And a contested row with its effect cleared constructs: it takes the
    seam path."""
    got = _run("""
from engine.season.manifest.registry import _declined_verbs
declined = _declined_verbs()
silent_ok = sorted(v for v, r in VERB_TABLE.items() if r.writes and v not in EFFECTS and v in declined)
both = sorted(v for v in declined if v in EFFECTS)
contested = sorted(v for v, r in VERB_TABLE.items() if r.contests and v in EFFECTS)
for v in contested:
    del EFFECTS[v]
print(repr((silent_ok, both, contested, construct())))
""")
    silent_ok, both, contested, refusal = got
    assert silent_ok and both and contested, (silent_ok, both, contested)
    assert refusal is None, refusal


def test_the_populated_realm_constructs_a_driver_and_every_check_ran():
    """Falsifier (7): `SeasonDriver(build_realm(0))` constructs -- and the registrar and both
    refusal sweeps RAN on it, observed by wrapping them, not inferred from the construction."""
    got = _run("""
import engine.season.manifest as M
from engine.season.harness.populated import build_realm
seen = {}
for name in ("register_module_entries", "check_rows", "check_contest_prizes", "check_effects"):
    real = getattr(M, name)
    def wrapped(*a, _real=real, _name=name, **k):
        out = _real(*a, **k)
        seen[_name] = len(out)
        return out
    setattr(M, name, wrapped)
w = build_realm(0)
SeasonDriver(w)
print(repr(seen))
""")
    assert set(got) == {"register_module_entries", "check_rows", "check_contest_prizes",
                        "check_effects"}, got
    assert got["check_rows"] and got["check_contest_prizes"] and got["check_effects"], got
    assert got["register_module_entries"] == 0, (
        f"{got['register_module_entries']} production row(s) registered; at `30` there are none "
        "(ID-13), and the first is `31a`'s -- re-read this test when one lands")


def test_the_composition_export_round_trips():
    """Falsifier (8), first half: the exporter's blocking `--check` re-derives `composition.json` and
    finds no drift, with every row's `entry:`/`verb:` cooked in."""
    out = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "export_composition.py"),
                          "--check"], capture_output=True, text=True, timeout=300)
    assert out.returncode == 0, out.stdout + out.stderr


def test_the_exporter_refuses_a_malformed_entry():
    """The exporter's own validation of `entry:` beside `kind:` -- each malformed shape refused."""
    import importlib.util
    import pytest
    spec = importlib.util.spec_from_file_location(
        "export_composition", os.path.join(ROOT, "tools", "export_composition.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    assert mod._check_entry("r", {"target": "a:b"}) == (None, None)
    assert mod._check_entry("r", {"entry": "verb_call", "verb": "tell"}) == ("verb_call", "tell")
    for bad in ({"entry": "no_such_entry"},
                {"entry": "verb_call"},
                {"entry": "query", "verb": "tell"},
                {"verb": "tell"},
                {"entry": "query", "kind": "value"}):
        with pytest.raises(SystemExit):
            mod._check_entry("r", bad)
