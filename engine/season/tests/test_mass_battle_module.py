"""THE `mass_battle` MODULE ENTRY, CALLED ON A HAND-BUILT RECORD -- plan position `31c` (IN-05), as
`test_combat_module.py` is `31b`'s and `test_social_contest_module.py` is `31a`'s.

A-25: a module takes the host's typed input record and a seeded `rng`, imports what it runs and the record
type and nothing else of the host, and never reads `World`. This test builds a `MassBattleInput` by hand --
no `World`, no driver, no registrar -- and calls the entry the way the host finds it: the prize row
`a field` names a composition role in `module_entry:` (`references/module_contracts.yaml`), whose `target:`
is the module's dotted path. Nothing here imports the module by name -- `engine/` never imports module code.

IN A FRESH SUBPROCESS, because what is asserted includes WHICH repository files the import loaded, and
inside a pytest process another test's imports have loaded the whole host already.

FALSIFIER (2) of `31c` -- nothing observed it before this file. ONE constructed `march` record resolved
twice in ONE process with one seed gives one result, WITH A DIFFERENT FIELD FOUGHT BETWEEN THE TWO CALLS:
module-level state surviving between calls (the engine's draw source, the geography cache, the trace
buffer -- the three `31c` shed) makes the second differ. Three more observations close the gaps that
determinism alone leaves open: the stdlib `random` stream is untouched by every call (the battle draws
only from the seeded `rng` its call scoped), no draw source is still scoped after a call returns, and the
seeds do not all give one result (else the comparison could not tell two calls apart).

AND THE MODULE OPENS NO FILE: `builtins.open`, `io.open` and `os.open` are watched from before the import
to the last call, and the set they saw must be empty -- the geography arrives on the record
(`MassBattleInput.geography`), read once per process by the host (`data/geography.py`); until it did,
`terrain.py` parsed the file on every fought field. The record's geography must also come back unwritten:
the host shares one mapping across every field.
"""
from __future__ import annotations

from ..data import files
from ._field_outcomes import SCALE            # the body scale the world ships (`Fixtures condition_scale`); a hand-built record names it
from ._fresh_process import entry_target, probe
from engine.dice_engine import draw

_PRIZE = "a field"

_PROBE = """
import sys, os, io, builtins, copy, importlib, random, yaml, dataclasses
sys.path.insert(0, {root!r})
# The geography the host hands the module on the record, read HERE, before anything is watched: the
# module takes it on `MassBattleInput.geography` and opens no file of its own.
with open(__GEOGRAPHY_YAML__, encoding="utf-8") as f:
    GEO = yaml.safe_load(f)
GEO_BEFORE = copy.deepcopy(GEO)
opened = []
def _watching(real):
    def watched(file, *a, **k):
        opened.append(str(file))
        return real(file, *a, **k)
    return watched
builtins.open, io.open, os.open = _watching(builtins.open), _watching(io.open), _watching(os.open)
before = set(sys.modules)
mod_name, attr = {target!r}.split(":", 1)
entry = getattr(importlib.import_module(mod_name), attr)
source = importlib.import_module(mod_name.rsplit(".", 1)[0] + ".rngsource")
from engine.season.queries.inputs import MassBattleInput
from engine.dice_engine import draw

# Sides large enough that the field is fought for ticks rather than routing on contact, on an UPHILL
# territory (T9) with a fortification (so the WALLS row and its DR are inside the replayed battle) and
# morale moved off the base by the stances.
FIELD = MassBattleInput(weights=((3.0, 2.0), (4.0,)), territory="T9", fort_level=1.0,
                        stances=(-1.0, 0.5), walls_dr=None, origin=None,
                        loyalties=(1.5, -0.5), loyalty_gain=0.4, geography=GEO, condition_scale=1000)
# A RIVER_CROSSING field (MB-05r): a march from T9 onto T3's open ground crosses the Valoris.
OTHER = MassBattleInput(weights=((3.0,), (2.0, 1.0)), territory="T3", fort_level=0.0,
                        stances=(0.0, 0.0), walls_dr=1, origin="T9",
                        loyalties=(0.0, 0.0), loyalty_gain=0, geography=GEO, condition_scale=1000)
stdlib_before = random.getstate()
out = []
for seed in (1, 2, 3, 4, 5, 6):
    got = entry(FIELD, draw.seeded(draw.H2("test_mass_battle_module", seed)))
    between = entry(OTHER, draw.seeded(draw.H2("test_mass_battle_module", seed + 100)))
    again = entry(FIELD, draw.seeded(draw.H2("test_mass_battle_module", seed)))
    try:
        source.get()                      # a scope left open by the call would return its draw here
        left_open = True
    except LookupError:                   # no source is the unscoped reading (there is no default stream)
        left_open = False
    out.append((seed, dataclasses.asdict(got), again == got, not left_open))
stdlib_untouched = random.getstate() == stdlib_before
loaded = sorted(os.path.relpath(m.__file__, {root!r}) for n, m in list(sys.modules.items())
                if n not in before and getattr(m, "__file__", None)
                and os.path.abspath(m.__file__).startswith({root!r} + os.sep))
print(repr((loaded, out, stdlib_untouched, opened, GEO == GEO_BEFORE)))
"""


def test_one_march_resolved_twice_in_one_process_gives_one_result_and_loads_nothing_of_the_host():
    role, target = entry_target(_PRIZE)
    loaded, out, stdlib_untouched, opened, geo_untouched = probe(
        _PROBE.replace("__GEOGRAPHY_YAML__", repr(str(files.GEOGRAPHY_YAML))), target, 600)
    module_dir = target.split(":", 1)[0].rsplit(".", 1)[0].replace(".", "/")
    allowed = {"engine/__init__.py", "engine/season/__init__.py", "engine/season/queries/__init__.py",
               "engine/season/queries/inputs.py", module_dir.split("/", 1)[0] + "/__init__.py"}
    # The dice engine is the one leaf the module imports besides the record type (B05.03, U5b §1 row 1): the
    # sampler and the ladder it draws from and grades on, as the other two registered modules already do.
    stray = [f for f in loaded if f not in allowed and not f.startswith("engine/dice_engine/")
             and not f.startswith(module_dir + "/")]
    assert not stray, (
        f"{role} ({target}) loaded repository code beyond the module it runs, the dice engine and the record type: {stray}. "
        "A-25: a module imports what it runs and the record types, nothing else of the host")
    assert f"{module_dir}/massbattle.py" in loaded and f"{module_dir}/orchestration.py" in loaded, loaded
    checked = 0
    for seed, got, deterministic, unscoped in out:
        assert set(got) == {"ended", "ticks", "attacker", "defender"} and got["ended"] in ("rout", "concession", "time"), got
        assert deterministic, f"{role}: seed {seed} gave two results in one process with a field between"
        assert unscoped, f"{role}: seed {seed} left a draw source scoped after the call returned"
        checked += 1
    assert checked == 6, checked
    assert stdlib_untouched, f"{role}: a call drew from the stdlib `random` stream, not its seeded rng"
    assert len({repr(got) for _, got, _, _ in out}) > 1, (
        "every seed fought the same field to the same result; the twice-in-one-process comparison cannot "
        "tell two calls apart")
    assert not opened, (
        f"{role} ({target}) opened {opened} while importing or fighting: the geography (and any other "
        "data) arrives on the record (`MassBattleInput.geography`, the host's one read), never by path")
    assert geo_untouched, f"{role} wrote into the record's geography, a mapping the host shares across fields"


def _fought(entry, seeds, rng_for):
    """Fight the two hand-built fields of the probe above, in this process, once per seed with `rng_for(seed)`."""
    import yaml
    from engine.season.queries.inputs import MassBattleInput
    with open(files.GEOGRAPHY_YAML, encoding="utf-8") as f:
        geo = yaml.safe_load(f)
    field = MassBattleInput(weights=((3.0, 2.0), (4.0,)), territory="T9", fort_level=1.0,
                            stances=(-1.0, 0.5), walls_dr=None, origin=None,
                            loyalties=(1.5, -0.5), loyalty_gain=0.4, geography=geo, condition_scale=SCALE)
    other = MassBattleInput(weights=((3.0,), (2.0, 1.0)), territory="T3", fort_level=0.0,
                            stances=(0.0, 0.0), walls_dr=1, origin="T9",
                            loyalties=(0.0, 0.0), loyalty_gain=0, geography=geo, condition_scale=SCALE)
    return [entry(inp, rng_for(seed)) for seed in seeds for inp in (field, other)]


def _entry():
    import importlib
    _role, target = entry_target(_PRIZE)
    mod_name, attr = target.split(":", 1)
    return getattr(importlib.import_module(mod_name), attr)


def test_no_d10_face_in_mass_battle():
    """DOE §1 gate (1), for the field: a graded act draws no d10 face. Two arms, each able to observe the failure it
    excludes: (a) the source of `modules/mass_battle` holds no d10-face draw (a `randint` over 1..10); (b) whole fields
    fought with a generator whose every d10-face `randint` over 1..10 RAISES come back, so the roll the field makes is the one
    sampler's `gauss` draw (a roll that still dealt faces would raise)."""
    import random
    import re
    from pathlib import Path

    root = Path(files.REPO_ROOT)
    scanned = 0
    for path in (root / "modules" / "mass_battle").rglob("*.py"):
        scanned += 1
        assert not re.search(r"(randint|die)\(\s*1\s*,\s*10\s*\)", path.read_text(encoding="utf-8")), path
    assert scanned >= 20, scanned

    class _NoFaces(draw.Draw):
        def __init__(self, seed):
            super().__init__(draw.H2("test_mass_battle_module", seed))

        def die(self, lo, hi):
            if (lo, hi) == (1, 10):
                raise AssertionError("a d10 face was drawn on the field")
            return super().die(lo, hi)

    fought = _fought(_entry(), range(1, 5), _NoFaces)
    assert len(fought) == 8 and all(type(got).__name__ == "FieldOutcome" for got in fought), fought
    assert len({repr(got) for got in fought}) > 1, "every field gave one result; the arm cannot tell fields apart"


def test_one_ladder_for_the_field(monkeypatch):
    """DOE §1 gate (2): the field grades on the owner's ladder and has none of its own. Two arms: (a) the module holds
    no ladder of its own (`compute_degree` and its epsilon are gone, nothing under `modules/mass_battle` spells the
    `net - ob` bands); (b) fought fields grade THROUGH `dice_engine.degree_from_net`, the one function a call to it
    is counted on, and every grade the field acted on is the owner's grade for that (net, ob)."""
    import importlib
    import re
    from pathlib import Path
    import random
    from engine.dice_engine import dice_engine

    _role, target = entry_target(_PRIZE)
    pkg = target.split(":", 1)[0].rsplit(".", 1)[0]
    entry = _entry()
    resolution = importlib.import_module(pkg + ".resolution")
    assert not hasattr(resolution, "compute_degree"), "the field still has a ladder of its own"
    assert not hasattr(resolution, "_DEGREE_EPS"), "the field still carries its own band epsilon"
    root = Path(files.REPO_ROOT)
    for path in (root / "modules" / "mass_battle").rglob("*.py"):
        assert not re.search(r"return\s+[\'\"](?:Overwhelming|Partial)[\'\"]", path.read_text(encoding="utf-8")), path

    seen = []
    real = dice_engine.degree_from_net

    def counting(net, ob, *a, **k):
        got = real(net, ob, *a, **k)
        seen.append((net, ob, got))
        return got

    monkeypatch.setattr(dice_engine, "degree_from_net", counting)
    _fought(entry, range(1, 4), lambda s: draw.seeded(draw.H2("test_mass_battle_module", s)))
    assert len(seen) >= 50, f"only {len(seen)} grade(s) went through the owner: the field grades elsewhere"
    assert all(got == real(net, ob) for net, ob, got in seen)


# ---- B17.01: ONE SURVIVOR SHARE, ONE SCALE, A DRAWN BATTLE -----------------------------------------------------

_SIDE_PAIRS = ((3, 2), (2, 1), (1, 2), (1.5, 1.5))     # B17.16: weights at 1,000 troops a weight (5,000 to 3,000)


def _headcount_record(weights):
    """A hand-built record of two headcount sides, one person each, on open ground (the `_fought` fields' geography)."""
    import yaml
    from engine.season.queries.inputs import MassBattleInput
    with open(files.GEOGRAPHY_YAML, encoding="utf-8") as f:
        geo = yaml.safe_load(f)
    return MassBattleInput(weights=((float(weights[0]),), (float(weights[1]),)), territory=None, fort_level=0.0,
                           stances=(0.0, 0.0), walls_dr=None, origin=None, loyalties=(0.0, 0.0), loyalty_gain=0,
                           geography=geo, condition_scale=SCALE, members=(("a",), ("b",)))


def test_no_share_exceeds_one():
    """B17.01 gate 1: a side's survivor share is `hp / hp_max` on every path, so it never exceeds 1.0. Four size
    pairs of headcount sides (`_weighted_unit`), seeds 0 to 39. An assertion that could not observe the failure is
    no assertion (CLAUDE.md §0.1 pt 2): the loop asserts that it asserted, and that a side the battle never touched
    reads EXACTLY 1.0 -- an unfought pair, graded through the one `_grade`, is that side."""
    import importlib
    mb = importlib.import_module("modules.mass_battle.massbattle")      # by string: `engine/` imports no module code
    entry, checked, worst = _entry(), 0, 0.0
    for pair in _SIDE_PAIRS:
        for seed in range(40):
            got = entry(_headcount_record(pair), draw.seeded(draw.H2("test_mass_battle_module", seed)))
            for share in (got.attacker.share / SCALE, got.defender.share / SCALE):
                assert share <= 1.0, f"{pair} seed {seed}: a side's share is {share}"
                worst = max(worst, share)
                checked += 1
    assert checked >= 320, checked
    # `_share` clamps to the scale, so the loop above cannot see a unit that ends above its start: read the raw armies. A unit
    # whose troops ended past its start is the failure this gate excludes (the retired `by_troops` read above 1.0).
    bl, raw = importlib.import_module("modules.mass_battle.orchestration"), 0
    rng_ = importlib.import_module("modules.mass_battle.rngsource")
    for pair in _SIDE_PAIRS:
        for seed in range(10):
            ra, rb = mb._weighted_unit("side_a", pair[0], "A"), mb._weighted_unit("side_b", pair[1], "B")
            with rng_.using(draw.seeded(draw.H2("test_mass_battle_module_raw", seed))):
                bl.run_battle(ra, rb, max_ticks=18)
            for u in ra.units + rb.units:
                assert u.cur_troops <= u._start_troops + 1e-9, (pair, seed, u.cur_troops, u._start_troops)
                raw += 1
    assert raw >= 40, raw
    a, b = mb._weighted_unit("side_a", 3, "A"), mb._weighted_unit("side_b", 2, "B")
    got = mb._grade(a, b, SCALE, 0)
    assert got.attacker.share == SCALE and got.defender.share == SCALE, got


def test_realm_weight_pairs_vary_by_seed():
    """B17.01 gate 2: at the scale one owner now gives (`under_arms_cap`), weights 3 v 2, 2 v 1 and 1 v 2
    through `resolve_field`, seeds 0 to 59, are fought battles whose verdict varies by seed, and the larger side wins
    more of them than the smaller. The verdict is the ladder's (`field_degree`, the one grader), read off what the
    module returned. A pair that always read one band would be a fixture, not a battle."""
    from engine.season.data.rosters import LOST, WON
    from engine.season.seam.ladder import field_degree
    entry, checked = _entry(), 0
    seen = set()
    for (wa, wb) in ((3, 2), (2, 1), (1, 2)):
        bands = [field_degree(entry(_headcount_record((wa, wb)), draw.seeded(draw.H2("test_mass_battle_module", seed)))) for seed in range(60)]
        checked += len(bands)
        seen |= set(bands)
        attacker_larger = wa > wb
        larger = bands.count(WON if attacker_larger else LOST)
        smaller = bands.count(LOST if attacker_larger else WON)
        assert larger > smaller, f"{wa} v {wb}: the larger side won {larger}, the smaller {smaller}: {bands}"
    assert checked >= 180, checked
    assert len(seen) >= 2, f"every field read one band: {seen}"


# ---- B17.16: A HEADCOUNT SIDE IS BUILT FROM SEVERAL UNITS --------------------------------------------------------

def _armies_fought(monkeypatch, inp, rng):
    """Fight `inp` through the module's entry and return the two `Army`s `run_battle` was handed, `(attacker, defender)`."""
    import importlib
    mb = importlib.import_module("modules.mass_battle.massbattle")
    seen, real = [], mb.run_battle

    def capturing(unit_a, unit_b, *a, **k):
        seen.append((unit_a, unit_b))
        return real(unit_a, unit_b, *a, **k)

    monkeypatch.setattr(mb, "run_battle", capturing)
    got = _entry()(inp, rng)
    assert len(seen) == 1 and not isinstance(got, dict), (len(seen), got)
    return seen[0]


def test_a_headcount_side_has_at_least_three_units_and_a_thousand_troops(monkeypatch):
    """B17.16 step 2 (ED-MB-0101): a headcount side that reaches the cell engine at or over the army's ruled floor is at least
    `MIN_UNITS_PER_ARMY` units and `MIN_ARMY_TROOPS` troops, on the `side` arm and on the `person` arm (one person, two, five),
    and every unit of it holds at least `MIN_CELLS_PER_UNIT` cells. One weight is the floor (1,000 troops). The loop asserts
    that it asserted (CLAUDE.md §0.1 pt 2)."""
    import dataclasses
    import importlib
    from engine.season.queries.inputs import MassBattleInput
    config = importlib.import_module("modules.mass_battle.config")
    checked = 0
    for units in ("side", "person"):
        for pair in ((1.0, 1.0), (3.0, 2.0), (6.0, 4.0), (12.0, 12.0)):
            inp = dataclasses.replace(_headcount_record(pair), units=units)
            for persons in (1, 2, 5):
                if persons > 1:
                    members = tuple(tuple(f"{s}{i}" for i in range(persons)) for s in "ab")
                    inp = dataclasses.replace(inp, members=members,
                                              weights=tuple(tuple(w / persons for _ in range(persons)) for w in pair))
                for army in _armies_fought(monkeypatch, inp, draw.seeded(draw.H2("test_mass_battle_module", 0))):
                    total = sum(u._start_troops for u in army.units)
                    assert len(army.units) >= config.MIN_UNITS_PER_ARMY, (units, pair, persons, len(army.units))
                    assert total >= config.MIN_ARMY_TROOPS, (units, pair, persons, total)
                    assert all(len(u.cell_start_troops) >= config.MIN_CELLS_PER_UNIT for u in army.units), (units, pair, persons)
                    checked += 1
    assert checked >= 20, checked


def test_no_unit_exceeds_the_per_unit_ceiling(monkeypatch):
    """B17.16 step 2: a headcount side past one unit's ceiling is split so that no unit holds more than
    `MAX_TROOPS_PER_UNIT`, and the side's troops are what they were (`under_arms_cap` of its weight, to the troop): the split
    loses and invents nobody. A person's units are named as one part: the `person` arm still names one part per member."""
    import dataclasses
    import importlib
    config = importlib.import_module("modules.mass_battle.config")
    cap = importlib.import_module("modules.mass_battle.troop_types.recruitment").under_arms_cap
    checked = 0
    for units in ("side", "person"):
        for pair in ((12.0, 9.0), (25.0, 25.0), (8.0, 40.0)):
            inp = dataclasses.replace(_headcount_record(pair), units=units)
            assert cap(max(pair)) > config.MAX_TROOPS_PER_UNIT or max(pair) < 11, "vacuous: no side is past one unit's ceiling"
            armies = _armies_fought(monkeypatch, inp, draw.seeded(draw.H2("test_mass_battle_module", 1)))
            for army, w in zip(armies, pair):
                assert all(u._start_troops <= config.MAX_TROOPS_PER_UNIT for u in army.units), (units, pair)
                assert abs(sum(u._start_troops for u in army.units) - cap(w)) < 1e-6, (units, pair)
                checked += 1
            got = _entry()(inp, draw.seeded(draw.H2("test_mass_battle_module", 1)))
            if units == "person":
                assert tuple(p.id for p in got.attacker.parts) == inp.members[0], got.attacker.parts
    assert checked >= 12, checked


# ---- B17.03: THE FIELD RETURNS A FROZEN `FieldOutcome` ---------------------------------------------------------

def test_resolve_field_returns_a_frozen_field_outcome():
    """B17.03 step 1 and 2: `resolve_field` returns a `FieldOutcome` on EVERY arm (the `side` arm, which names no part, and
    the `person` arm, which names each member's); it is frozen; each side's `share` and each part's are integers on the body
    scale, `0..scale`; the `person` arm's parts are the members in input order, and `broke_first` names one of them or nobody.
    The loop asserts that it asserted (CLAUDE.md §0.1 pt 2): a `person` field that named no part would pass every per-part
    line vacuously."""
    import dataclasses
    from engine.season.queries.inputs import FieldOutcome, PartOutcome, SideOutcome
    entry, parts_seen, fields = _entry(), 0, 0
    for units in ("side", "person"):
        for seed in range(8):
            inp = dataclasses.replace(_headcount_record((3, 2)), units=units)
            got = entry(inp, draw.seeded(draw.H2("test_mass_battle_module", seed)))
            fields += 1
            assert type(got) is FieldOutcome, f"{units}: the arm returned {type(got).__name__}"
            assert got.ended in ("rout", "concession", "time") and isinstance(got.ticks, int) and got.ticks >= 1, got
            for field in dataclasses.fields(got):
                try:
                    setattr(got, field.name, getattr(got, field.name))
                except dataclasses.FrozenInstanceError:
                    continue
                raise AssertionError(f"FieldOutcome.{field.name} is writable: the record is not frozen")
            for side, members in zip((got.attacker, got.defender), inp.members):
                assert type(side) is SideOutcome and type(side.share) is int and 0 <= side.share <= SCALE, side
                assert isinstance(side.routed, bool) and isinstance(side.conceded, bool), side
                if units == "side":
                    assert side.parts == () and side.broke_first is None, side
                    continue
                assert tuple(part.id for part in side.parts) == members, (side.parts, members)
                for part in side.parts:
                    assert type(part) is PartOutcome and type(part.share) is int and 0 <= part.share <= SCALE, part
                    assert isinstance(part.routed, bool), part
                    parts_seen += 1
                assert side.broke_first in (None, *members), side.broke_first
    assert fields == 16 and parts_seen == 16, (fields, parts_seen)


def test_ended_outside_its_set_is_refused():
    """B17.03 step 1: `FieldOutcome.__post_init__` refuses an `ended` outside `'rout' | 'concession' | 'time'`. CONTROL, the
    same record built with each member of the set: it is accepted, so the refusal is the set's and not the record's."""
    import pytest
    from engine.season.queries.inputs import FieldOutcome, SideOutcome
    side = SideOutcome(share=SCALE, routed=False, conceded=False, parts=(), broke_first=None)
    for ended in ("rout", "concession", "time"):
        assert FieldOutcome(ended=ended, ticks=1, attacker=side, defender=side).ended == ended
    for bad in ("draw", "won", "", None, "Rout"):
        with pytest.raises(ValueError):
            FieldOutcome(ended=bad, ticks=1, attacker=side, defender=side)


def test_an_untouched_side_reads_exactly_the_scale_and_the_share_quantises_float_noise():
    """B17.03 step 1: a share is `round(scale x hp_left / hp_start)`, so the engine's float noise is quantised away AT THE SEAM.
    A side the battle never touched reads EXACTLY the scale (an unfought pair, graded through the one `_grade`), and a ratio
    that is one part in 10^15 short of 1 (an untouched unit reads 0.9999999999999987 off `_person_report`'s float division, which
    cost an untouched winner a body under `int(body x ratio)`) reads the scale too: `int(1000 * 0.9999999999999987)` is 999,
    `_share(...)` is 1000. A share never leaves `0..scale`."""
    import importlib
    mb = importlib.import_module("modules.mass_battle.massbattle")
    got = mb._grade(mb._weighted_unit("side_a", 3, "A"), mb._weighted_unit("side_b", 2, "B"), SCALE, 0)
    assert (got.attacker.share, got.defender.share) == (SCALE, SCALE) and got.ended == "time", got
    noisy = 0.9999999999999987
    assert noisy < 1.0 and int(SCALE * noisy) == SCALE - 1, "vacuous: the noise no longer costs a body under int()"
    assert mb._share(noisy * 450.0, 450.0, SCALE) == SCALE
    assert mb._share(0.0, 450.0, SCALE) == 0 and mb._share(451.0, 450.0, SCALE) == SCALE


# ---- B17.04: A SIDE PAST THE CEILING, OR OF NOBODY, NEVER REACHES THE CELL ENGINE ------------------------------------

def _count_run_battle(monkeypatch):
    """Wrap `massbattle.run_battle` (the cell engine's entry) in a counter; returns the one-slot list the count lands in."""
    import importlib
    mb = importlib.import_module("modules.mass_battle.massbattle")
    entered, real = [0], mb.run_battle

    def counting(*a, **k):
        entered[0] += 1
        return real(*a, **k)

    monkeypatch.setattr(mb, "run_battle", counting)
    return entered


def _oob_record(troops_a, troops_b):
    """A hand-built record of two sides each holding ONE-unit order of battle of the troops named (B17.16: a headcount side is cut
    below the ceiling, so the only unit past it is an order's own row). `drawn` is empty: the battle reads none of it."""
    import dataclasses
    import importlib
    mb = importlib.import_module("modules.mass_battle.massbattle")
    row = lambda n: mb.OrderOfBattle((mb.UnitRow("line", "light_infantry", float(n)),))
    return dataclasses.replace(_headcount_record((1, 1)), orders_of_battle=(row(troops_a), row(troops_b)))


def test_past_the_ceiling_returns_scale_gap(monkeypatch):
    """B17.04 step 1: a unit past `config.MAX_TROOPS_PER_UNIT` is refused with `status="SCALE-GAP"` (a dict, on `PARTY-GAP`'s
    shape) and `run_battle` is not entered; `SCALE-GAP` is a member of the seam's `REFUSAL_STATUSES`, so `contest()` reads it as a
    refusal and not as a software defect. CONTROL, the same record with the unit AT the ceiling: it resolves to a `FieldOutcome`
    through `run_battle`, so the refusal is the ceiling's and not the record's. The boundary is the ceiling itself: 10,000 troops
    resolve, 10,020 do not. B17.16: the arm that reaches the ceiling is an order of battle's row; a headcount side is cut into
    units under it (`massbattle._cut`), so no weight reaches it (asserted last)."""
    import importlib
    from engine.season.queries.inputs import FieldOutcome
    from engine.season.seam.contest import REFUSAL_STATUSES, _returned
    config = importlib.import_module("modules.mass_battle.config")
    cap = config.MAX_TROOPS_PER_UNIT
    entry, entered = _entry(), _count_run_battle(monkeypatch)
    got = entry(_oob_record(cap + 20, cap + 20), draw.seeded(draw.H2("test_mass_battle_module", 0)))
    assert isinstance(got, dict) and got["status"] == "SCALE-GAP" and got["why"], got
    assert entered == [0], f"run_battle entered {entered[0]} time(s) on a side past the ceiling"
    assert "SCALE-GAP" in REFUSAL_STATUSES
    refused = _returned(dict(got, module="mass_battle"), "a field", "test")
    assert (refused.status, refused.why) == ("SCALE-GAP", got["why"]), refused
    # one side alone past the ceiling refuses the field too
    got = entry(_oob_record(cap, cap + 20), draw.seeded(draw.H2("test_mass_battle_module", 0)))
    assert isinstance(got, dict) and got["status"] == "SCALE-GAP", got
    # CONTROL
    got = entry(_oob_record(cap, 3000), draw.seeded(draw.H2("test_mass_battle_module", 0)))
    assert isinstance(got, FieldOutcome) and entered == [1], (got, entered)
    # a headcount side of a hundred weight (100,000 troops) is not past the ceiling: it is cut under it
    got = entry(_headcount_record((100, 2)), draw.seeded(draw.H2("test_mass_battle_module", 0)))
    assert isinstance(got, FieldOutcome), got
    # ... and one that needs more than `armies.UNIT_CAP` units to stay under it is past the ceiling, refused and not built
    got = entry(_headcount_record((112, 2)), draw.seeded(draw.H2("test_mass_battle_module", 0)))
    assert isinstance(got, dict) and got["status"] == "SCALE-GAP", got


def test_a_person_side_of_more_than_the_unit_cap_is_refused_not_fought():
    """An army holds at most `armies.UNIT_CAP` units. The `person` arm builds one unit per person at least, so twelve persons of one
    weight are twelve units however small: SCALE-GAP and `run_battle` is not entered. CONTROL: eleven persons are fought."""
    import importlib
    from dataclasses import replace
    from engine.season.queries.inputs import FieldOutcome
    cap = importlib.import_module("modules.mass_battle.armies").UNIT_CAP
    entry = _entry()
    def record(n):
        base = _headcount_record((1, 1))
        ids = tuple(f"p{i}" for i in range(n))
        return replace(base, weights=(tuple(1.0 for _ in ids), (1.0,)), members=(ids, ("b",)), units="person")
    got = entry(record(cap + 1), draw.seeded(draw.H2("test_mass_battle_module", 0)))
    assert isinstance(got, dict) and got["status"] == "SCALE-GAP", got
    got = entry(record(cap), draw.seeded(draw.H2("test_mass_battle_module", 0)))
    assert isinstance(got, FieldOutcome), got


def test_empty_sides_never_reach_run_battle(monkeypatch):
    """B17.04 step 2: a field of nobody against nobody (a weight of 0) and one of two sides at the crash floor (one man a side,
    `_MIN_TROOPS`) return `status="PARTY-GAP"` and never enter `run_battle`. The floor holds only for BOTH sides: CONTROL, a real
    side against a floor-sized one (the attacker marching on a thin garrison) is fought as it always was, through `run_battle`."""
    import importlib
    from engine.season.queries.inputs import FieldOutcome
    cap = importlib.import_module("modules.mass_battle.troop_types.recruitment").under_arms_cap
    entry, entered = _entry(), _count_run_battle(monkeypatch)
    assert cap(0.0) == 0 and cap(0.001) == 1, "vacuous: the probe weights are not nobody and one man"
    for pair in ((0.0, 0.0), (0.001, 0.001), (0.0, 0.001), (0.001, 0.0)):
        got = entry(_headcount_record(pair), draw.seeded(draw.H2("test_mass_battle_module", 0)))
        assert isinstance(got, dict) and got["status"] == "PARTY-GAP" and got["why"], (pair, got)
    assert entered == [0], f"run_battle entered {entered[0]} time(s) on a field of nobody"
    for pair in ((3.0, 0.0), (0.001, 3.0)):
        got = entry(_headcount_record(pair), draw.seeded(draw.H2("test_mass_battle_module", 0)))
        assert isinstance(got, FieldOutcome), (pair, got)
    assert entered == [2], entered
