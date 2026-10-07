"""THE REGISTRAR AND THE DRIVER-CONSTRUCTION REFUSALS -- plan position `30` (A-25; `ED-IN-0284`,
revised by `ED-IN-0285`). One planted violation per refusal, EACH IN A FRESH SUBPROCESS.

WHY A SUBPROCESS PER CASE. `MODULE_ENTRIES` (`engine/season/manifest/registrar.py`), `PROVIDERS`
(`manifest/providers.py`) and `EFFECTS` (`loop/effects_shared.py`) are process globals: inside a
pytest process another test's imports can fill them, so an in-process test can pass on a table it
did not build. `tests/valoria/test_season_providers_are_registered.py` is the precedent.

SUBJECT, under `CLAUDE.md` §0.1 pt 5: these are the loader's refusals per data family
(`CLAUDE.md` §0.05, "the loader's refusal per data family") over rows the game resolves from -- the
composition rows, the prize rows and the verb rows. Refusal (a) and the second half of (c) replace a
path by which a verb used to leave the game without a word. (b), (d) and the unbacked-entry refusal
guard the entries `31a` onward declare and have no production row to refuse at `30` (`ID-13`, below);
the first half of (c) repeats a refusal `data/verbs.py` already makes at load.

`ID-13`, READ EXACTLY: no production composition row carries `entry:` at `30`, so every registrar
case below PLANTS one; the registrar's pass over production rows is first exercised at `31a`.

The plan's falsifiers, by number (`workplans/valoria_master_workplan_v9_part4.md`, IN-02 = position `30`):
(2) `test_a_registered_row_deleted_under_a_live_process_refuses_naming_it` -- ONLY ITS WITHIN-PROCESS
FORM (plant, construct, delete, construct): in a fresh process a deleted row leaves nothing to refuse
on, since no data at `30` declares that a row must exist, so the fresh-process form is `31a`'s to place
(its falsifier 3) -- and `test_a_verb_call_row_naming_no_verb_refuses_naming_it` (refusal (b)); (3) `test_a_prize_row_with_its_provider_cleared_refuses_naming_the_prize`;
(4) `test_a_verb_contesting_a_prize_no_row_claims_refuses_naming_the_verb`; (5)
`test_a_writing_row_with_its_effect_cleared_refuses_naming_the_verb`; (6) the two
`test_one_entry_registered_twice_*` and `test_two_verb_call_rows_for_one_verb_refuse`; (7) `test_the_populated_realm_constructs_a_driver_and_every_check_ran`;
(8) `test_the_composition_export_round_trips`, with
`test_engine_does_not_import_systems.py::test_importing_every_engine_module_pulls_in_no_subsystem`.

Plan position IN-41 (`SM-11` + `SM-9`; `_part4`), which split the retired `decline_note:` column into
`effect_decline_note:`, `formation_decline_note:` and `requires_decline_note:`: falsifier (1)
`test_a_row_with_an_untyped_precondition_nothing_evaluates_refuses_naming_the_verb`, with its converse
`test_a_row_whose_precondition_is_evaluable_and_declined_refuses_naming_the_verb`; falsifier (2)
`test_a_row_with_an_effect_and_an_effect_declining_note_refuses_naming_the_verb`, and its "`oblige` and
`destroy_record` construct" half in
`test_refusal_a_covers_contested_rows_and_lets_every_declared_row_construct`.
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


def _run(body: str, head: str = _HEAD):
    """Run `head` + `body` in a fresh interpreter; `body` prints one `repr(...)`, returned evaluated."""
    out = subprocess.run([sys.executable, "-c", head.format(root=ROOT) + body],
                         capture_output=True, text=True, timeout=600)
    assert out.returncode == 0, out.stderr[-3000:]
    return eval(out.stdout.strip().splitlines()[-1])     # our own probe's repr


def _assert_refused(refusal, *names):
    assert refusal is not None, f"driver construction did NOT refuse; expected it to name {names}"
    kind, text = refusal
    assert kind == "Unspecified", refusal
    for n in names:
        assert n in text, f"the refusal does not name {n!r}: {text}"


#: Imports NOTHING from `engine.season` -- the row is planted before the driver and the manifest are
#: imported, which is what lets a test see a registrar wired at import: it would run on that plant and
#: `MODULE_ENTRIES` would be non-empty before any driver is constructed.
_HEAD_BEFORE_THE_SEASON_IMPORTS = """
import sys
sys.path.insert(0, {root!r})
import yaml
from engine.substrate import composition

TARGET = "engine.dice_engine.dice_engine:degree_from_net"
_doc = yaml.safe_load(open({root!r} + "/engine/season/verb_table.yaml"))
_verbs = sorted(str(r["verb"]) for r in _doc["verbs"])
composition.ROLES["planted.entry"] = dict(
    target=TARGET, kind="callable", entry="verb_call", verb=_verbs[0],
    needed_by="planted by tests/valoria/test_module_registrar.py")

from engine.season.loop.driver import SeasonDriver, EFFECTS, VERB_TABLE
from engine.season.state.world import World
from engine.season.manifest import MODULE_ENTRIES

def construct():
    try:
        SeasonDriver(World(0))
        return None
    except Exception as exc:
        return (type(exc).__name__, str(exc))
"""


def test_a_planted_entry_is_registered_by_string_at_construction_and_idempotently():
    """The registrar's positive half: a row with `entry:` is in `MODULE_ENTRIES` after construction,
    resolved to the target's callable, and NOT before it -- the row was planted BEFORE the driver and
    the manifest were imported (`_HEAD_BEFORE_THE_SEASON_IMPORTS`), so a registrar that ran at import
    would have filled the table by then; constructing again refuses nothing and leaves the one table
    unchanged."""
    got = _run("""
verb = _verbs[0]
before = sorted(MODULE_ENTRIES)
first = construct()
after = {r: (e.entry, e.verb, e.target, e.fn.__name__) for r, e in MODULE_ENTRIES.items()}
second = construct()
again = {r: (e.entry, e.verb, e.target, e.fn.__name__) for r, e in MODULE_ENTRIES.items()}
print(repr((verb, before, first, after, second, again)))
""", head=_HEAD_BEFORE_THE_SEASON_IMPORTS)
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


def test_two_verb_call_rows_for_one_verb_refuse():
    """Refusal (d)'s second form -- [ASSUMPTION, `SM-5`]: which module a verb calls has one answer, so
    two `verb_call` rows (two different targets) for one verb are refused. Two entries, not one
    registered twice; the rule is the registrar's reading of A-25's *\"two owners say which module is
    called\"*, and `SM-5` (a grid or map variant as its own module) is what could change it."""
    refusal = _run("""
verb = sorted(VERB_TABLE)[0]
plant("planted.one", verb)
plant("planted.two", verb, target="engine.dice_engine.dice_engine:degree_label")
print(repr(construct()))
""")
    _assert_refused(refusal, "planted.one", "planted.two")


def test_one_entry_registered_twice_by_a_second_writer_refuses():
    """Refusal (d): the table already holds the role, bound by something other than the registrar.
    The planted entry differs from its row in the CALLABLE only (same target), so the refusal must
    show both entries whole -- naming the targets alone would read "holds X and now names X"."""
    refusal = _run("""
from engine.season.manifest import ModuleEntry
verb = sorted(VERB_TABLE)[0]
plant("planted.entry", verb)
MODULE_ENTRIES["planted.entry"] = ModuleEntry("planted.entry", "verb_call", verb, TARGET, print)
print(repr(construct()))
""")
    _assert_refused(refusal, "planted.entry", "registered twice", "built-in function print",
                    "degree_from_net")


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
    """Falsifier (5), refusal (a): clear the effect of a writing row that carries no
    `effect_decline_note:`. Chosen from the tables -- a writing, uncontested row with an effect and no
    decline -- not named."""
    got = _run("""
verb = sorted(v for v, r in VERB_TABLE.items()
              if r.writes and not r.contests and v in EFFECTS and not r.effect_decline_note)[0]
del EFFECTS[verb]
print(repr((verb, construct())))
""")
    verb, refusal = got
    _assert_refused(refusal, repr(verb), "effect_decline_note")


#: The rows whose `verb_table.yaml` entry carries `formation_decline_note:` -- an annotation the loader
#: does not load into `VerbRow` (its `*_note` rule), so it is read off the file here.
_FORMATION_DECLINED = """
import yaml
_doc = yaml.safe_load(open({root!r} + "/engine/season/verb_table.yaml"))
formation_declined = sorted(str(r["verb"]) for r in _doc["verbs"]
                            if str(r.get("formation_decline_note") or "").strip())
"""


def test_refusal_a_covers_contested_rows_and_lets_every_declared_row_construct():
    """Refusal (a)'s reach, observed. A writing row with no effect that carries an
    `effect_decline_note:` constructs (every shipped such row does); a row whose note declines its
    FORMATION (`formation_decline_note:` -- `oblige`, `destroy_record`, derived from the file, not
    named) HAS an effect and constructs, which is what the `SM-9` split exists to allow. And a
    CONTESTED writing row is not exempt: it routes to the seam and then folds the result through
    `EFFECTS` (`loop/resolve.py::_contest` -> `_fold`), so clearing its effect is refused, naming it --
    while a contested row that writes nothing (`tell`) needs no effect and is not named."""
    got = _run(_FORMATION_DECLINED.format(root=ROOT) + """
silent_ok = sorted(v for v, r in VERB_TABLE.items()
                   if r.writes and v not in EFFECTS and r.effect_decline_note)
formation_with_effect = sorted(v for v in formation_declined if v in EFFECTS)
control = construct()
contested_writers = sorted(v for v, r in VERB_TABLE.items() if r.contests and r.writes and v in EFFECTS)
contested_no_write = sorted(v for v, r in VERB_TABLE.items() if r.contests and not r.writes)
for v in contested_writers:
    del EFFECTS[v]
print(repr((silent_ok, formation_declined, formation_with_effect, control, contested_writers,
            contested_no_write, construct())))
""")
    (silent_ok, formation_declined, formation_with_effect, control, contested_writers,
     contested_no_write, refusal) = got
    assert silent_ok and formation_declined and contested_writers and contested_no_write, got
    assert formation_with_effect == formation_declined, (
        f"a formation-declined row has no effect, so the split is not what this test observes: {got}")
    assert control is None, control          # the shipped state (declined rows of both kinds) constructs
    _assert_refused(refusal, "effect_decline_note", *[repr(v) for v in contested_writers])
    for v in contested_no_write:
        assert repr(v) not in refusal[1], (v, refusal)


def test_a_row_with_an_effect_and_an_effect_declining_note_refuses_naming_the_verb():
    """IN-41 falsifier (2), refusal (a)'s CONVERSE arm (`SM-9`): plant an `effect_decline_note:` on a
    writing row that HAS an effect -- chosen from the tables, not named. Before the split this arm
    could not be armed, because `oblige` and `destroy_record` carried an effect and a `decline_note:`
    that declined their formation."""
    got = _run("""
import dataclasses
verb = sorted(v for v, r in VERB_TABLE.items() if r.writes and v in EFFECTS)[0]
VERB_TABLE[verb] = dataclasses.replace(VERB_TABLE[verb], effect_decline_note="planted")
print(repr((verb, construct())))
""")
    verb, refusal = got
    _assert_refused(refusal, repr(verb), "effect_decline_note", "HAVE an effect")


def test_a_row_with_an_untyped_precondition_nothing_evaluates_refuses_naming_the_verb():
    """IN-41 falsifier (1), `check_preconditions` (`SM-11`): un-type a row whose precondition a TYPED
    CELL evaluates (and no `REQUIRES_PREDICATES` entry does), with no `requires_decline_note:` --
    chosen from the tables, not named. Before IN-41 `resolvable_verbs()` dropped such a row without a
    word; the control is that the same row is in that set before the plant and out of it after."""
    got = _run("""
import dataclasses
from engine.season.loop.driver import REQUIRES_PREDICATES, resolvable_verbs
from engine.season.data.verbs import NO_PRECONDITION
verb = sorted(v for v, r in VERB_TABLE.items()
              if r.requires.strip() not in NO_PRECONDITION and r.requires_typed is not None
              and v not in REQUIRES_PREDICATES and not r.requires_decline_note)[0]
before = verb in resolvable_verbs()
VERB_TABLE[verb] = dataclasses.replace(VERB_TABLE[verb], requires_typed=None)
after = verb in resolvable_verbs()
print(repr((verb, before, after, construct())))
""")
    verb, before, after, refusal = got
    assert before and not after, f"the plant did not move {verb!r} out of resolvable_verbs(): {got}"
    _assert_refused(refusal, repr(verb), "nothing evaluates", "requires_decline_note")


def test_a_row_whose_precondition_is_evaluable_and_declined_refuses_naming_the_verb():
    """`check_preconditions`'s CONVERSE arm, refusal (a)'s shape one gate over: plant a
    `requires_decline_note:` on a row a registered predicate evaluates -- chosen from the tables, not
    named. A note saying nothing evaluates a precondition that something does is a stale declaration."""
    got = _run("""
import dataclasses
from engine.season.loop.driver import REQUIRES_PREDICATES
verb = sorted(v for v in VERB_TABLE if v in REQUIRES_PREDICATES)[0]
VERB_TABLE[verb] = dataclasses.replace(VERB_TABLE[verb], requires_decline_note="planted")
print(repr((verb, construct())))
""")
    verb, refusal = got
    _assert_refused(refusal, repr(verb), "requires_decline_note", "IS evaluable")


def test_every_shipped_row_dropped_on_its_precondition_says_why():
    """`SM-11`'s positive half on the shipped tree: every row `resolvable_verbs()`'s first gate drops
    carries a `requires_decline_note:`, and the shipped tree constructs -- derived, not listed. A
    vacuous sweep (no such row) would observe nothing, so it asserts there is at least one."""
    got = _run("""
from engine.season.loop.driver import REQUIRES_PREDICATES
dropped = sorted(v for v, r in VERB_TABLE.items() if not r.precondition_evaluable(REQUIRES_PREDICATES))
unsaid = [v for v in dropped if not VERB_TABLE[v].requires_decline_note]
print(repr((dropped, unsaid, construct())))
""")
    dropped, unsaid, control = got
    assert dropped, "no shipped row is dropped on its precondition; this test observes nothing"
    assert unsaid == [], unsaid
    assert control is None, control


def test_the_populated_realm_constructs_a_driver_and_every_check_ran():
    """Falsifier (7): `SeasonDriver(build_realm(0))` constructs -- and the registrar and both
    refusal sweeps RAN on it, observed by wrapping them, not inferred from the construction."""
    got = _run("""
import engine.season.manifest as M
from engine.season.harness.populated import build_realm
seen = {}
for name in ("register_module_entries", "check_rows", "check_contest_prizes", "check_effects",
             "check_preconditions"):
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
                        "check_effects", "check_preconditions"}, got
    assert (got["check_rows"] and got["check_contest_prizes"] and got["check_effects"]
            and got["check_preconditions"]), got
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
    assert mod._check_entry("r", {"entry": "query"}) == ("query", None)
    for bad, said in (({"entry": "no_such_entry"}, "must be one of"),
                      ({"entry": "verb_call"}, "names its verb"),
                      ({"entry": "verb_call", "verb": ""}, "names its verb"),
                      ({"entry": "verb_call", "verb": ["tell"]}, "names its verb"),
                      ({"entry": "query", "verb": "tell"}, "names its verb"),
                      ({"entry": "query", "verb": ""}, "names its verb"),
                      ({"verb": "tell"}, "with no `entry:`"),
                      ({"entry": "query", "kind": "value"}, "kind: value")):
        with pytest.raises(SystemExit, match=said):
            mod._check_entry("r", bad)
