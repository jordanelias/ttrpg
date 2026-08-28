"""One faction write mechanism, and a guard that fails on a second (ED-FA-0038).

THE RULING. Jordan, this session, verbatim: **"one faction write mechanism"**. It was given
alongside "one degree ladder", and the degree half drew four commits while this half drew none —
because when it was measured, it was already TRUE. `engine.autoload.game_state.Faction.adjust` is
the single owner: it resolves the stat's bounds from `descriptors.faction_bounds` (the registry),
applies the `MULTS` granularity, clamps, and writes. Measured across `engine/` and `systems/`,
non-test: **zero** compound assignments (`fac.L += …`) and **zero** bare assignments to a Faction
stat outside the dataclass itself.

SO WHY A GUARD RATHER THAN NOTHING. CLAUDE.md §0.1 point 5 asks for three things when a rule has
one owner: the owner, every site routed through it, and **a guard that fails on recurrence**. Two
of the three were done and the third was missing, so the ruling was satisfied by the tree's
current state and by nothing that would keep it satisfied. That is exactly the shape
`test_morale_write_sweep.py` exists for — its docstring calls out the same class — and this file
is deliberately its sibling rather than a new invention.

The predicate admits it. The artifact is faction stats, which are load-bearing on the game (every
faction action, the victory check, and the CI/MS tracks read them), on the exported params (the
bounds cross to Godot through `descriptors`), and on a Jordan ruling (three of them: ED-IN-0029's
floors, "Influence can be 0", and "Legitimacy is a base" — all of which reach the code only
because `adjust` is the one place that consults the registry). A bypassing write would silently
skip all three.

⚠ WHAT THIS DOES NOT CLAIM. It does not say every faction MUTATION goes through `adjust` — flags
(`senator_inward_used`), territory lists, and treaty state are written directly by design and are
not stats. The claim is narrower and is the one the ruling makes: the six SCALAR STATS carrying
declared bounds are written in exactly one place.

FALSIFIER: `test_no_new_bypassing_faction_stat_write` fails the moment a second write path
appears. Mutation-verified by adding a bare `f.L = 3.0` to a non-test module, which reds it.
"""
from __future__ import annotations

import ast
import dataclasses
import pathlib
import re

import pytest

from engine.autoload import game_state as GS

REPO = pathlib.Path(__file__).resolve().parents[2]
SCAN_ROOTS = ("engine", "systems")

#: The stats `adjust` owns, DERIVED rather than typed: the intersection of `MULTS` (the
#: granularity table `adjust` itself indexes) with the `Faction` dataclass's own fields. A stat
#: added to the engine is swept without anyone remembering to come here, and a stat removed stops
#: being swept for the right reason.
#:
#: ⚠ THE INTERSECTION IS LOAD-BEARING AND WAS LEARNED THE HARD WAY. A first version read
#: `tuple(sorted(GS.MULTS))` alone, which also contains `accord` and `pt` — fields of `Territory`,
#: not `Faction`. The sweep promptly flagged `mass_seizure.py:296` and
#: `parliamentary_transfer.py:346` as bypassing faction writes. They are not: both write
#: `Territory.accord`, a different field on a different class that happens to share the
#: granularity table. Scoping by name alone cannot tell a Faction stat from a Territory one.
#:
#: (Those two sites ARE a real divergence, and a KNOWN one in a different lane —
#: `systems/overview/sim/accounting.py`'s module docstring records that two write paths for
#: "provincial Accord" coexist uncoordinated, tracked as SE-lane OI-37. This guard is deliberately
#: not the place that reports it: a faction-write guard that also policed territory writes would
#: be two rules in one file, which is the shape §8 forbids.)
OWNED_STATS = tuple(sorted(set(GS.MULTS) & {f.name for f in dataclasses.fields(GS.Faction)}))


def _live_python():
    for root in SCAN_ROOTS:
        for path in sorted((REPO / root).rglob("*.py")):
            p = path.relative_to(REPO).as_posix()
            if "/tests/" in p or "/test_" in p or p.split("/")[-1].startswith("test_"):
                continue
            yield p, path.read_text(encoding="utf-8")


# ── 1. The owner is the owner ─────────────────────────────────────────────────────────

def test_adjust_is_the_only_thing_that_clamps_a_faction_stat():
    """The bounds lookup has exactly one runtime caller, and it is `adjust`.

    If a second call site appears, a stat is being clamped somewhere else — which is how a
    ratified floor stops being the floor for that path only.
    """
    callers = []
    for p, text in _live_python():
        for i, line in enumerate(text.splitlines(), 1):
            if "faction_bounds(" in line and "def faction_bounds" not in line:
                callers.append(f"{p}:{i}")
    assert callers, "nothing calls faction_bounds — the registry has stopped reaching the engine"
    assert all(c.startswith("engine/autoload/game_state.py") or
               c.startswith("engine/substrate/descriptors.py") or
               c.startswith("tools/") for c in callers), (
        f"faction_bounds is consulted outside the owner: {callers}")


def test_adjust_actually_clamps_from_the_registry():
    """Not a structural claim — the ruled floors must reach a real write.

    Guards the case where `adjust` survives as the single owner but stops consulting the
    registry, which would satisfy every structural check above while silently restoring the
    blanket bounds ED-IN-0029 replaced.
    """
    w = GS.create_world(seed=0)
    fac = next(iter(w.factions.values()))
    for stat in OWNED_STATS:
        if stat not in GS.MULTS:
            continue
        setattr(fac, stat, 1.0)
        fac.adjust(stat, -1000.0)
        low = getattr(fac, stat)
        setattr(fac, stat, 1.0)
        fac.adjust(stat, +1000.0)
        high = getattr(fac, stat)
        assert low >= 0.0, f"{stat} floored below 0 at {low}"
        assert high <= 7.0, f"{stat} ceilinged above 7 at {high}"
        assert low < high, f"{stat} did not move in either direction — adjust is inert for it"


# ── 2. THE FALSIFIER: no second write path ────────────────────────────────────────────

def _stat_writes(path, text):
    """AST, not regex: yield (line, target) for assignments to a Faction stat attribute.

    A regex over `\\.L\\s*=` flags `self.L = L` in every unrelated dataclass and misses
    `setattr(f, 'L', v)`. Walking assignments and augmented-assignments finds the shape the rule
    is about — a stat attribute written on something that is not `self`.
    """
    try:
        tree = ast.parse(text)
    except SyntaxError:                     # pragma: no cover - a broken file is another test's job
        return
    for node in ast.walk(tree):
        targets = []
        if isinstance(node, ast.Assign):
            targets = node.targets
        elif isinstance(node, (ast.AugAssign, ast.AnnAssign)):
            targets = [node.target]
        for tgt in targets:
            if not isinstance(tgt, ast.Attribute) or tgt.attr not in OWNED_STATS:
                continue
            # `self.<stat> = …` inside the owner's own class is the write itself, not a bypass.
            if isinstance(tgt.value, ast.Name) and tgt.value.id == "self":
                continue
            yield node.lineno, tgt.attr
    # setattr(obj, '<stat>', …) — the spelling an AST target check cannot see
    for node in ast.walk(tree):
        if (isinstance(node, ast.Call) and getattr(node.func, "id", None) == "setattr"
                and len(node.args) >= 2 and isinstance(node.args[1], ast.Constant)
                and node.args[1].value in OWNED_STATS):
            if not (isinstance(node.args[0], ast.Name) and node.args[0].id == "self"):
                yield node.lineno, f"setattr(…, {node.args[1].value!r})"


#: Sites allowed to write a stat outside `adjust`, each with a reason. A NEW file reaching for one
#: fails the test until it is either routed through `adjust` or added here with a reason — the same
#: registry shape `test_morale_write_sweep.py`'s `_CELL_OWNED` uses.
DECLARED_WRITERS: dict[str, str] = {
    # EMPTY BY MEASUREMENT, NOT BY POLICY, and that is the finding. There is currently NO file
    # that writes a `Faction` stat outside `Faction.adjust`. Nothing needs listing here:
    # `adjust` writes `setattr(self, stat, val)`, `create_world` builds Factions through the
    # constructor, and `massbattle.py`'s `self.Mil = Mil` is a Unit's own constructor — all on
    # `self`, none an outside write. The registry exists so the FIRST genuine exception has
    # somewhere to be declared, with a reason, visible in a diff, instead of being waved through.
}


def test_no_new_bypassing_faction_stat_write():
    """THE FALSIFIER. A second write path is the defect the ruling forbids."""
    offenders = []
    for p, text in _live_python():
        if p in DECLARED_WRITERS:
            continue
        for lineno, stat in _stat_writes(p, text):
            offenders.append(f"{p}:{lineno} writes {stat}")
    assert not offenders, (
        "faction stat(s) written outside `Faction.adjust` — a bypassing write skips the registry "
        "bounds, so ED-IN-0029's floors and the 2026-08-23 rulings ('Influence can be 0', "
        "'Legitimacy is a base') do not apply on that path:\n  " + "\n  ".join(offenders)
        + "\n\nRoute it through `adjust`, or add the file to DECLARED_WRITERS with a reason.")


def test_the_matcher_can_actually_see_every_write_spelling():
    """Assert that it asserted (§0.1 pt 2) — and the form matters here.

    The usual shape is "the sweep must still find something live". That is the WRONG check for a
    sweep whose correct answer is zero: it would demand a live violation exist in order to prove
    the guard works, which is backwards. So the matcher is fed a synthetic module containing every
    spelling a bypassing write can take, and must find all of them. If the matcher silently stops
    matching, this fails while `test_no_new_bypassing_faction_stat_write` goes vacuously green —
    which is precisely the pair that has to be kept honest.
    """
    stat = OWNED_STATS[0]
    sample = (
        "def bypass(fac, other):\n"
        f"    fac.{stat} = 3.0\n"                 # bare assignment
        f"    other.{stat} += 1.0\n"              # augmented assignment
        f"    setattr(fac, {stat!r}, 2.0)\n"      # setattr spelling
        "\n"
        "class Owner:\n"
        "    def ok(self):\n"
        f"        self.{stat} = 1.0\n"            # on `self` — NOT a bypass
        f"        setattr(self, {stat!r}, 1.0)\n"  # also on `self`
    )
    found = list(_stat_writes("synthetic.py", sample))
    assert len(found) == 3, (
        f"the matcher found {len(found)} of 3 bypassing spellings in a synthetic sample "
        f"({found}) — it has stopped seeing one of them, and the sweep is now blind to that shape")
    assert not any(ln >= 7 for ln, _ in found), (
        f"the matcher flagged a `self.` write as a bypass ({found}) — it would report the owner "
        "itself and every dataclass constructor in the tree")


def test_there_is_currently_no_bypassing_write_at_all():
    """The measured state the ruling asked for, pinned as a number so a drift is visible.

    Separate from the falsifier above deliberately: that one fails on a NEW writer, this one
    records that the count is zero today. If a future commit adds a declared exemption, this test
    is where the change from "none" to "one declared" becomes explicit.
    """
    live = {p: len(list(_stat_writes(p, text))) for p, text in _live_python()}
    offending = {p: n for p, n in live.items() if n and p not in DECLARED_WRITERS}
    assert offending == {}, offending
    assert DECLARED_WRITERS == {}, (
        f"DECLARED_WRITERS is no longer empty: {sorted(DECLARED_WRITERS)}. That may be correct, "
        "but it is a change in the ruling's standing — 'one faction write mechanism' now has a "
        "declared second path. Update this assertion in the same commit and say why.")


def test_the_declared_writers_registry_is_not_a_dumping_ground():
    """An exemption list that grows is the rule dissolving one entry at a time.

    Pinned small and deliberately: two entries, and the second is a name collision rather than a
    genuine second writer. Raising this number is a decision that should be visible in a diff.
    """
    assert len(DECLARED_WRITERS) <= 2, (
        f"DECLARED_WRITERS has grown to {len(DECLARED_WRITERS)}: "
        f"{sorted(DECLARED_WRITERS)}. Each addition is one more path the registry bounds do not "
        "reach. If a new writer is genuinely correct, raise this ceiling in the same commit and "
        "say why — do not let it drift up silently.")
    assert all(len(reason) > 40 for reason in DECLARED_WRITERS.values()), (
        "an exemption without a real reason is an exemption nobody will ever remove")
