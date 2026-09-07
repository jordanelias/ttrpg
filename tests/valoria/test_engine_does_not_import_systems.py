"""`engine/` must not name `systems/`. As of 2026-08-22 none does — at module level OR inside a
function — and this pins both counts at zero so neither can grow back.

THE PREMISE (Jordan, 2026-08-20): **`systems/` stems from `engine/` and `references/`.** `engine/`
is the root — the executable model and the single owner of each rule — and `systems/<sub>/sim/`
composes on top of it. A top-level `from systems...` inside `engine/` inverts that: the root names
its own dependents, and the package graph acquires a cycle.

WHAT WAS MEASURED, 2026-08-20. `CLAUDE.md` §3 claimed the dependency graph is "acyclic, autoload is
a leaf". It is neither. Six non-test modules under `engine/` imported `systems.*` at module level,
and `engine/autoload/game_state.py` imports seven subsystems' state classes inside functions —
deferred imports hide a cycle from the interpreter, they do not remove it.

The concrete cycle was `systems/factions/sim/faction_action.py:42` imports
`engine.autoload.game_state` while `game_state.py` imports `systems.factions.sim.treaty`.

CLOSED 2026-08-22 (plan S5a), IN TWO COMMITS AND NOT ONE, because the plan's own instruction was
wrong on this point. S5a said to delete the cycle guard "when `BASELINE_TOTAL` hits 0". Doing so
would have cleared the guard on a claim that was still FALSE: the cycle's engine-side half was
`game_state.py`'s NESTED import of `treaty`, which `BASELINE_TOTAL` never counted. The first commit
took the module-level count to 0 and said so here rather than deleting anything; the second took
the nested count to 0 as well, and only then did the guard invert — from
`test_the_documented_cycle_is_still_real` (a text match recording a live defect) to
`test_importing_engine_pulls_in_no_subsystem` (a subprocess import probe measuring the property).

⚠ THE ENGINE STILL DEPENDS ON SUBSYSTEMS. The dependencies are DECLARED in
`references/module_contracts.yaml` and resolved by string at first call, which is the point: the
IMPORT GRAPH is acyclic and a subsystem can be swapped by editing a registry row, but nothing here
says the engine runs without `systems/`. Do not read a green suite as that claim.

WHY THIS IS A RATCHET AND NOT A CLIFF. A hard "zero imports" assertion would be red on arrival and
would be deleted within a session. `ALLOWED` is a ceiling that can only go DOWN: each seam that
moves to registration-driven composition deletes its line here, in the same commit, and a NEW
inversion fails immediately. That is the same shape as `.godot-compile-baseline` in the port.

SUBJECT, under `CLAUDE.md` §0.1 pt 5's load-bearing predicate: the architecture of the executable
model that the Godot port is generated against — the game, not this repository's process. It earns
its existence. It is also the falsifier §0.1 pt 3 requires for the claim "the direction is being
inverted": without it, the last seam removed would be silently re-added by the next session.

`engine/tests/` is exempt. A test may reach across any boundary to set up a case; that is what tests
are for, and forbidding it would only push the reach into a fixture.
"""
from __future__ import annotations

import pathlib
import ast
import re

REPO = pathlib.Path(__file__).resolve().parents[2]
ENGINE = REPO / 'engine'

# Top-level `from systems...` / `import systems...` — column 0 only. An import nested inside a
# function is a DIFFERENT (and also real) problem, counted separately BELOW — not merely promised to
# be. Conflating the two counts would make the top-level list churn on refactors that change nothing
# about the package graph; leaving the nested one UNCOUNTED, which is what this file did until
# 2026-08-21, is worse than conflating them (see NESTED_BASELINE).
TOP_LEVEL_SYSTEMS_IMPORT = re.compile(r'^(?:from|import)\s+systems[.\s]', re.M)

# The same import, indented — i.e. inside a function or a class body. A deferred import hides the
# cycle from the interpreter; it does not remove it. `engine/autoload/game_state.py` carried ELEVEN
# of them, which is what made "autoload is a leaf" false until 2026-08-22.
NESTED_SYSTEMS_IMPORT = re.compile(r'^[ \t]+(?:from|import)\s+systems[.\s]', re.M)

# THE CEILING. Every entry is a seam to be moved to registration-driven composition
# (proposals/2026-08-20-return-to-game-plan-v1.md Act C3). Remove the line when the seam lands.
# NEVER add one.
# EMPTY, as of 2026-08-22 (plan S5a). All three seams landed:
#   Seam 1 (cross_scale/echo_transport.py, 2026-08-20) — imported systems.settlements.sim.registry
#     for STAT_MIN/STAT_MAX alone, a 0-5 bound that references/descriptor_registry.yaml already
#     declares as `set.order`, so it reads the root via engine.substrate.descriptors instead.
#   Seam 2 (mc_v18.py, 2026-08-20) — the campaign driver's two subsystem callbacks resolve through
#     engine.substrate.composition, with references/module_contracts.yaml's composition_roles:
#     block naming the providers.
#   Seam 3 (cross_scale/parliamentary_bridge.py, 2026-08-22) — the §10 vote, its two record types
#     and the territory-transfer entry points resolve as roles; the transfer DERIVATION moved to
#     its owner (systems/factions/sim/parliamentary_transfer.derive_transfer_candidate), because it
#     read four members private to that module. The lateral duplicate of the same seam, at
#     parliamentary_transfer.py:54, went in the same commit — one seam, one declaration.
#
# AN EMPTY ALLOW-LIST IS NOT THE END OF THE JOB, AND THIS PARAGRAPH ONCE SAID SO ABOUT A DIFFERENT
# NUMBER. `NESTED_BASELINE` reached 0 in the commit after the one that emptied this list, and a
# THIRD instrument exists below it — `PATH_SEAM_ALLOWED`, for the seam that is not an import at all.
# Do not read `BASELINE_TOTAL == 0` as "engine/ no longer depends on systems/": it depends on them
# as much as ever, through roles declared in `references/`.
ALLOWED = {}
BASELINE_TOTAL = 0

# THE SECOND CEILING, AND THE REASON IT EXISTS. With only the count above, the CHEAPEST way to lower
# `BASELINE_TOTAL` is to indent a top-level import into the function that uses it. That satisfies the
# ratchet, reads as progress in a commit message, and makes the cycle HARDER to see — the metric's
# cheapest satisfier makes the underlying condition worse. Counting both means the move is net-zero:
# the top-level number falls, this one rises, and only genuine removal lowers the pair.
#
# Measured 2026-08-21: game_state.py 11, scene_dispatch.py 4, echo_transport.py 1 — the eleven in
# `autoload` being the `engine -> systems` half of the then-live package cycle with
# `systems/factions/sim/faction_action.py:42`. All sixteen moved to composition roles on
# 2026-08-22 (plan S5a). ZERO IS NOW A FLOOR, NOT A WAYPOINT: this ceiling can no longer be
# lowered, only violated, so any rise is a new deferred seam and must be justified in the plan.
NESTED_BASELINE = 0


def _offenders():
    found = {}
    for path in sorted(ENGINE.rglob('*.py')):
        rel = path.relative_to(ENGINE).as_posix()
        if rel.startswith('tests/') or '__pycache__' in rel:
            continue
        hits = TOP_LEVEL_SYSTEMS_IMPORT.findall(path.read_text(encoding='utf-8'))
        if hits:
            found[rel] = len(hits)
    return found


def _nested_offenders():
    found = {}
    for path in sorted(ENGINE.rglob('*.py')):
        rel = path.relative_to(ENGINE).as_posix()
        if rel.startswith('tests/') or '__pycache__' in rel:
            continue
        hits = NESTED_SYSTEMS_IMPORT.findall(path.read_text(encoding='utf-8'))
        if hits:
            found[rel] = len(hits)
    return found


def test_no_new_engine_to_systems_inversion():
    found = _offenders()
    new = sorted(set(found) - set(ALLOWED))
    assert not new, (
        'NEW engine/ -> systems/ import(s): ' + ', '.join(new) + '\n'
        'engine/ is the root; systems/ stems from it. Compose through an engine.substrate '
        'registration point instead of naming the subsystem, or if this seam genuinely cannot move '
        'yet, say so in the plan and add it here deliberately — never as a drive-by.'
    )


def test_the_allow_list_can_only_shrink():
    found = _offenders()
    stale = sorted(set(ALLOWED) - set(found))
    assert not stale, (
        'These seams no longer import systems/: ' + ', '.join(stale) + '\n'
        'Good — delete them from ALLOWED and lower BASELINE_TOTAL in this same commit. A stale '
        'ceiling is how a ratchet stops ratcheting.'
    )


def test_the_total_did_not_rise():
    total = sum(_offenders().values())
    assert total <= BASELINE_TOTAL, (
        f'engine/ -> systems/ imports ROSE {BASELINE_TOTAL} -> {total}.'
    )
    assert total == BASELINE_TOTAL, (
        f'engine/ -> systems/ imports FELL {BASELINE_TOTAL} -> {total}. Lower BASELINE_TOTAL to '
        f'{total} in this commit so the progress is banked.'
    )


def test_nested_systems_imports_did_not_rise():
    """The deferred-import count is a ceiling too, so hiding a seam is not progress."""
    total = sum(_nested_offenders().values())
    assert total <= NESTED_BASELINE, (
        f'function-local engine/ -> systems/ imports ROSE {NESTED_BASELINE} -> {total}. Moving a '
        f'top-level import inside a function does not remove the cycle; it hides it. If a seam '
        f'genuinely has to defer, remove one elsewhere or say why here.'
    )
    assert total == NESTED_BASELINE, (
        f'function-local engine/ -> systems/ imports FELL {NESTED_BASELINE} -> {total}. Lower '
        f'NESTED_BASELINE to {total} in this commit so the progress is banked.'
    )


def test_the_two_counts_cannot_be_gamed_against_each_other():
    """The falsifier for the ratchet itself (§0.1 pt 3): indenting an import must be observable.

    Without this, the pair of ceilings is just two numbers. This asserts the specific property that
    makes them a ratchet rather than a scoreboard — that the SAME line, at column 0 and indented,
    is seen by exactly one pattern each, so a move between them is visible as a change in both.
    """
    line = 'from systems.factions.sim import treaty\n'
    assert TOP_LEVEL_SYSTEMS_IMPORT.search(line)
    assert not NESTED_SYSTEMS_IMPORT.search(line)
    assert not TOP_LEVEL_SYSTEMS_IMPORT.search('    ' + line)
    assert NESTED_SYSTEMS_IMPORT.search('    ' + line)


def test_this_check_can_observe_its_own_failure(tmp_path):
    """An assertion that cannot observe the failure it excludes is an absent assertion (§0.1 pt 2)."""
    probe = tmp_path / 'probe.py'
    probe.write_text('from systems.factions.sim import treaty\n')
    assert TOP_LEVEL_SYSTEMS_IMPORT.search(probe.read_text())
    nested = tmp_path / 'nested.py'
    nested.write_text('def f():\n    from systems.factions.sim import treaty\n')
    assert not TOP_LEVEL_SYSTEMS_IMPORT.search(nested.read_text()), \
        'the pattern must not fire on a function-local import — that is a different problem'


#: The ONE surviving seam, declared rather than invisible. `engine/cross_scale/combat_bridge.py`
#: inserts `systems/combat/combat_engine_v1/` onto `sys.path` and imports `combatant` and `wrapper`
#: by BARE NAME. It was invisible to every instrument in this file until 2026-08-22: both regexes
#: look for the literal token `systems`, and the import probe below used to filter `sys.modules` by
#: the `systems.` prefix — under which those two modules appear as `combatant` and `wrapper`.
#:
#: WHY IT IS NOT CONVERTED HERE. `combat_engine_v1/` is a FLAT, self-contained module set with its
#: own convention: `wrapper.py:4` inserts its own directory on `sys.path` and bare-imports its
#: siblings, and the workbench and audit harnesses all load it that way. Importing it by dotted path
#: works, but would give those modules a SECOND identity in any process that also loads them the
#: flat way — `workbench/balance.py` is the canonical balance harness and does exactly that. That is
#: a PC-lane convention change with a module-identity hazard, not an IN-lane wiring fix, and it is
#: out of scope for a step whose subject is the composition registry.
#:
#: It can only shrink. Converting it deletes this entry.
#: SECOND ENTRY ADDED 2026-09-05 (ED-IN-0202, the adoption). `season/combat_seam.py` is the SAME
#: seam from the season loop's side, into the same flat module set, following combat_bridge's
#: discipline deliberately (its own header cites it as precedent). It is declared rather than
#: converted for the identical reason the first entry gives: dotted-path loading would give
#: `wrapper`/`combatant` a second identity in a process that also loads them flat, which the
#: balance workbench does. Still shrink-only: converting either one deletes its entry.
PATH_SEAM_ALLOWED = {'cross_scale/combat_bridge.py', 'season/combat_seam.py'}


def _inserts_a_systems_path(text):
    """True iff this module puts a path NAMING `systems` onto `sys.path` — which is the seam.
    Reads the inserted expression, not the file's word soup, and follows one level of local
    assignment (`_PC = _REPO / "systems" / ...` then `sys.path.insert(0, str(_PC))`)."""
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return False
    assigned = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name):
                    assigned[t.id] = ast.get_source_segment(text, node.value) or ""
    names_re = re.compile(r"""['"]systems['"]|/systems/""")
    for node in ast.walk(tree):
        if not (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)):
            continue
        if node.func.attr not in ("insert", "append"):
            continue
        if ast.unparse(node.func.value).replace(" ", "") not in ("sys.path", "path"):
            continue
        for arg in node.args:
            expr = ast.get_source_segment(text, arg) or ""
            seen = set()
            while expr:
                if names_re.search(expr):
                    return True
                try:
                    nxt = [n.id for n in ast.walk(ast.parse(expr, mode="eval"))
                           if isinstance(n, ast.Name) and n.id in assigned and n.id not in seen]
                except SyntaxError:
                    break
                if not nxt:
                    break
                seen.update(nxt)
                expr = " ".join(assigned[n] for n in nxt)
    return False


def _modules_loaded_from_systems(probe_body):
    """Run `probe_body` in a subprocess and return the modules it loaded whose FILE lives under
    `systems/` — regardless of what they are called in `sys.modules`."""
    import subprocess
    import sys

    probe = (
        'import sys, os\n'
        + probe_body +
        "\nroot = os.path.join(os.path.abspath('.'), 'systems') + os.sep\n"
        "bad = sorted(f'{n}<-{getattr(m, \"__file__\", \"\")}' for n, m in list(sys.modules.items())\n"
        "            if getattr(m, '__file__', None) and str(m.__file__).startswith(root))\n"
        "print('|'.join(bad))\n"
    )
    proc = subprocess.run([sys.executable, '-c', probe], cwd=str(REPO),
                          capture_output=True, text=True)
    assert proc.returncode == 0, f'the probe did not run:\n{proc.stderr}'
    return [m for m in proc.stdout.strip().split('|') if m]


def test_importing_every_engine_module_pulls_in_no_subsystem():
    """THE CLAIM, MEASURED OVER THE WHOLE PACKAGE AND BY FILE PATH (§0.2).

    Two corrections to the first version of this test, both found by a read-only adversarial pass
    on 2026-08-22 and both of which made it weaker than the docstring claimed:

    1. IT IMPORTED FIVE HAND-PICKED MODULES. A subsystem import in any other module under `engine/`
       was seen only if it was literally spelled `import systems`. It now walks EVERY module under
       `engine/` (excluding `engine/tests/`) and imports them all in one subprocess.

    2. IT FILTERED `sys.modules` BY THE NAME `systems.`, so it could not see the one seam that
       matters — `combat_bridge.py` puts `systems/combat/combat_engine_v1/` on `sys.path` and
       imports `combatant`/`wrapper` by bare name, which land in `sys.modules` under those names
       and were counted as clean. It now asks each loaded module where its FILE is. A module's
       path cannot be spelled around; its import name can.

    `PATH_SEAM_ALLOWED` above is the ceiling for what remains, and it is one entry.
    """
    mods = []
    for path in sorted((REPO / 'engine').rglob('*.py')):
        rel = path.relative_to(REPO / 'engine').as_posix()
        if rel.startswith('tests/') or '__pycache__' in rel or rel.endswith('__init__.py'):
            continue
        mods.append('engine.' + rel[:-3].replace('/', '.'))
    assert len(mods) >= 20, f'only {len(mods)} engine modules discovered — the walk is broken'

    body = 'import importlib\n' + ''.join(
        f'importlib.import_module({m!r})\n' for m in mods)
    leaked = _modules_loaded_from_systems(body)
    assert not leaked, (
        'importing engine/ loaded ' + str(len(leaked)) + ' module(s) whose file is under systems/: '
        + ', '.join(leaked) + '\n'
        'engine/ is the root; systems/ stems from it. Resolve the dependency through a composition '
        'role (references/module_contracts.yaml) instead of importing it.'
    )


def test_the_one_declared_path_seam_is_still_the_only_one():
    """`combat_bridge` reaches into `systems/` by `sys.path` + bare name. That is a real seam and it
    is DECLARED here rather than left invisible — the ratchet's own rule is that a seam which cannot
    move yet is added deliberately, with its reason, never as a drive-by.

    Scans for the mechanism rather than the module: any `sys.path` mutation in `engine/` that names
    `systems`. A second one is a new seam of the class that hid for two days.
    """
    offenders = {}
    for path in sorted((REPO / 'engine').rglob('*.py')):
        rel = path.relative_to(REPO / 'engine').as_posix()
        if rel.startswith('tests/') or '__pycache__' in rel:
            continue
        text = path.read_text(encoding='utf-8')
        # ⚠ TWO DEFECTS FOUND AT THE 2026-09-05 ADOPTION, BOTH IN THIS PREDICATE.
        # (1) It was `"'systems'" in text` — a SINGLE-QUOTED literal only — so
        #     `season/combat_seam.py`'s `_REPO / "systems" / ...` was invisible and this guard
        #     stayed green while a second undeclared seam existed. Matching on TYPOGRAPHY rather
        #     than on the concept is the defect this file exists to prevent one level down.
        # (2) Widening the quoting alone then reported `season/shape.py`, which is NOT a seam: it
        #     inserts the REPO ROOT to import `engine.autoload.dice_engine` by dotted path, and
        #     `systems` appears elsewhere in it as a directory probe for a diagnostic string.
        #     Co-occurrence ANYWHERE IN THE FILE was never the right question. An over-refusal is
        #     a defect of equal weight to a miss: it would push a later author to delete a
        #     legitimate dotted import.
        # So the predicate now asks what is actually INSERTED — the argument expression of each
        # `sys.path.insert/append`, following one level of local assignment.
        if _inserts_a_systems_path(text):
            offenders[rel] = True
    assert set(offenders) == PATH_SEAM_ALLOWED, (
        f'sys.path seams into systems/ are now {sorted(offenders)}, declared {sorted(PATH_SEAM_ALLOWED)}. '
        f'A NEW one is the invisible-seam class: it defeats both regexes above AND the import probe, '
        f'because the modules it loads are not named `systems.*`. Removing one? Delete it from '
        f'PATH_SEAM_ALLOWED in the same commit.'
    )


def test_the_import_probe_can_observe_both_kinds_of_leak():
    """§0.1 pt 2 — the probe must be able to FAIL, and in BOTH the ways it is supposed to catch.
    Its whole result is "the list was empty", which is also what a broken probe returns.

    Two planted leaks, because the probe was rewritten precisely because it caught only the first:
      1. a normal dotted `import systems.…`;
      2. the `sys.path` + BARE NAME shape `combat_bridge` uses, where the loaded module is called
         `wrapper`, not `systems.combat.…`. The old name-prefix probe reported this one as clean.
    """
    dotted = _modules_loaded_from_systems('import systems.factions.sim.faction_action\n')
    assert dotted, 'the probe reports NOTHING for a plain dotted import — it is broken'

    bare = _modules_loaded_from_systems(
        "sys.path.insert(0, os.path.join(os.path.abspath('.'), 'systems', 'combat', "
        "'combat_engine_v1'))\nimport combatant\n")
    assert bare, (
        'the probe reports NOTHING for a module loaded by sys.path + bare name. That is the exact '
        'seam it was rewritten to see; a name-prefix filter cannot, because the module is called '
        '"combatant".'
    )
    assert any('combatant' in b for b in bare), bare


def test_the_composition_resolver_refuses_an_undeclared_role():
    """The indirection must not degrade into a silent default.

    §0.1 pt 2: an assertion that cannot observe its failure is absent. The failure this design could
    introduce is a campaign running with a subsystem quietly missing, so `require()` raises on an
    undeclared role rather than returning None — and that behaviour is pinned here.
    """
    import pytest

    from engine.substrate import composition
    with pytest.raises(KeyError) as exc:
        composition.require('no_such_role')
    assert 'do not' in str(exc.value).lower(), 'the error must tell the reader not to work around it'


def test_every_role_game_state_requires_is_declared():
    """The check the INTERPRETER used to do for free, restored after the indirection removed it.

    Before S5a, `engine/autoload/game_state.py`'s eleven seams were function-local imports. A typo
    in one was a hard `ImportError` the moment that branch ran, and a moved class was caught at
    import. Routing them through `composition.require('snapshot_state.knots')` turns both into a
    STRING, and a mistyped string is a `KeyError` raised only when that branch executes — i.e. only
    when a save file happens to carry that registry non-empty. Nine of the ten `restore_world`
    branches have no test that reaches them (only `settlements` round-trips, in
    `engine/tests/test_world_population.py`), so a typo would ship green.

    This is not a new rung: it re-asserts, mechanically, the property the static imports asserted.
    Subject is `engine/`'s save/restore path and the registry the Godot port's serialization is
    generated against — load-bearing on the game (§0.1 pt 5), not on this repo's process.
    """
    from engine.substrate import composition

    gs = (REPO / 'engine' / 'autoload' / 'game_state.py').read_text(encoding='utf-8')
    required = set(re.findall(r"composition\.require\(\s*['\"]([^'\"]+)['\"]\s*\)", gs))
    assert len(required) == 11, (
        f'game_state.py requires {len(required)} distinct roles, expected 11 — the eleven seams '
        f'S5a moved. If a seam was legitimately added or removed, update this count deliberately.'
    )
    undeclared = sorted(required - set(composition.ROLES))
    assert not undeclared, (
        'game_state.py requires composition role(s) that references/module_contracts.yaml does '
        'not declare: ' + ', '.join(undeclared) + '. This raises KeyError at runtime, in the '
        'branch that needs it — which for a snapshot registry means only when a save file carries '
        'it non-empty. Declare the row and re-run tools/export_composition.py.'
    )


def test_every_snapshot_state_role_resolves_to_something_restore_world_can_call():
    """`restore_world` calls `.from_dict(...)` on every class it resolves. A row pointing at a
    callable WITHOUT that method exports cleanly — the exporter only checks callability — and then
    raises `AttributeError` in the same unreachable branch. Assert the contract the caller relies
    on, not merely that the target exists."""
    from engine.substrate import composition

    snapshot_roles = sorted(r for r in composition.ROLES if r.startswith('snapshot_state.'))
    assert len(snapshot_roles) == 10, (
        f'{len(snapshot_roles)} snapshot_state roles, expected 10 — one per registry '
        f'`restore_world` rehydrates.'
    )
    for role in snapshot_roles:
        cls = composition.require(role)
        assert hasattr(cls, 'from_dict'), (
            f'{role} -> {composition.ROLES[role]["target"]} has no from_dict(), but '
            f'restore_world calls it. The row is wrong, or the class lost the method.'
        )


def test_no_snapshot_state_role_is_declared_and_unused():
    """A declared row nobody requires is the ED-IN-0149 defect — an abstraction with no caller.
    Pairs with the two above so the registry and the engine cannot drift apart in either
    direction: an undeclared requirement fails there, an unrequired declaration fails here."""
    from engine.substrate import composition

    gs = (REPO / 'engine' / 'autoload' / 'game_state.py').read_text(encoding='utf-8')
    required = set(re.findall(r"composition\.require\(\s*['\"]([^'\"]+)['\"]\s*\)", gs))
    declared = {r for r in composition.ROLES if r.startswith('snapshot_state.') or r == 'world_gen_settlements'}
    orphans = sorted(declared - required)
    assert not orphans, (
        'composition role(s) declared for game_state.py that it never requires: '
        + ', '.join(orphans) + '. Delete the row, or wire it.'
    )


def test_a_value_role_still_fails_on_an_attribute_that_does_not_exist():
    """The falsifier for the ONE guard S5a relaxed (§0.1 pt 2, pt 5's "a guard must earn it").

    `_resolve` used to reject any target that was not callable. Two roles now declare
    `kind: value` — `systems.social_contest.sim.contest`'s side labels `A`/`B`, which
    `scene_dispatch.py` compares a verdict against and which no callable role could carry. Relaxing
    a guard to fit the case in front of you is how guards die, so this pins what SURVIVED the
    relaxation: a `value` row is still resolved at export time, and a target naming an attribute
    that does not exist still fails the blocking gate.

    Without this, `kind: value` would be a hole: any typo'd constant name would export cleanly and
    then compare false forever at runtime, silently — which for `contest_side.a` means the
    emergency-council echo quietly degrades to 'Partial' and only a golden diff ever says so.
    """
    import importlib.util
    import pytest

    spec = importlib.util.spec_from_file_location(
        'export_composition', REPO / 'tools' / 'export_composition.py')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    # A real module, a constant that is not there.
    with pytest.raises(SystemExit) as exc:
        mod._resolve('systems.social_contest.sim.contest:NO_SUCH_CONSTANT', 'value')
    assert 'has no' in str(exc.value)

    # And the callable guard is intact for every row that did NOT opt out.
    with pytest.raises(SystemExit) as exc2:
        mod._resolve('systems.social_contest.sim.contest:A', 'callable')
    assert 'non-callable' in str(exc2.value)

    # The real rows still resolve, in both kinds.
    assert mod._resolve('systems.social_contest.sim.contest:A', 'value') is not None
    assert callable(mod._resolve('systems.social_contest.sim.contest:build_contest', 'callable'))


def test_only_the_two_contest_side_labels_are_value_roles():
    """`kind: value` exists for a named, argued reason. If a third one appears, that is either a
    genuine new case worth stating in the plan, or the widening spreading by imitation — which is
    exactly how the callable guard would be lost without anyone deciding to lose it."""
    from engine.substrate import composition

    value_roles = sorted(r for r, row in composition.ROLES.items() if row.get('kind') == 'value')
    assert value_roles == ['contest_side.a', 'contest_side.b'], (
        f'value-kind composition roles are now {value_roles}. Adding one is a deliberate act: say '
        f'in the plan why no callable role and no authored surface can carry it, then update this '
        f'list. Both earlier constant seams were solved WITHOUT a value role.'
    )


def test_every_declared_composition_role_resolves():
    """Import-by-string is only safe because every target is proven to resolve. Prove it here too,
    so the guarantee does not live solely in a tool a session might not run."""
    from engine.substrate import composition
    assert composition.ROLES, 'no composition roles declared - mc_v18 has nothing to resolve'
    for role, row in composition.ROLES.items():
        resolved = composition.require(role)
        if row.get('kind') == 'value':
            # A constant. It must RESOLVE (require() raises if the row or attribute is wrong);
            # asserting callability here would assert the opposite of what the row declares.
            # `test_only_the_two_contest_side_labels_are_value_roles` is what stops this branch
            # from quietly becoming the majority.
            continue
        assert callable(resolved), f'role {role} did not resolve to a callable'
    assert sum(1 for r in composition.ROLES.values() if r.get('kind') != 'value') >= 20, (
        'the callable branch above checked almost nothing - most roles should be callables'
    )


# ---------------------------------------------------------------------------------------------
# DECISION 1 STEP A (ED-IN-0202, 2026-09-05): "only ... social contests, personal combat and mass
# battles to be retained. All work in /engine is retained as well." 19 of the 27 declared
# composition roles above target one of the twelve subsystems that ruling does NOT retain
# (`references/module_contracts.yaml`'s composition_roles: block). Retiring those subsystems is
# Step B, gated on R-04, and has not happened — this ceiling only makes the count SHRINK-ONLY, the
# same shape as `ALLOWED`/`PATH_SEAM_ALLOWED` above: a role LEAVING the set is Step B progress and
# needs no update here; a role ENTERING it — a NEW seam into a subsystem Jordan ruled out — is
# drift during a retirement window and must fail.
R04_PENDING_SUBSYSTEMS = {
    '_architecture', 'articulation', 'characters', 'factions', 'fieldwork', 'npcs', 'overview',
    'settlements', 'threadwork', 'ui', 'victory', 'world',
}

R04_PENDING_ROLES = {
    'faction_action', 'season_driver', 'accounting', 'territory_transfer_candidate',
    'territory_transfer_proposal', 'world_gen_settlements', 'snapshot_state.practitioners',
    'snapshot_state.insurgencies', 'snapshot_state.npcs', 'snapshot_state.treaties',
    'snapshot_state.convictions', 'snapshot_state.beliefs', 'snapshot_state.knots',
    'snapshot_state.territory_infrastructure', 'snapshot_state.threadcut_beings',
    'snapshot_state.settlements', 'scene_resolver.fieldwork', 'scene_resolver.investigation',
    'rs_track_delta',
}


def test_r04_pending_composition_roles_can_only_shrink():
    from engine.substrate import composition
    live = {role for role, row in composition.ROLES.items()
            if row['target'].split('.', 2)[1] in R04_PENDING_SUBSYSTEMS}
    new = sorted(live - R04_PENDING_ROLES)
    assert not new, (
        'NEW composition role(s) target a non-retained subsystem during the ED-IN-0202 retirement '
        'window: ' + ', '.join(new) + '. This is the exact collision Decision 1 Step A named — '
        'engine/ naming more of the twelve superseded subsystems is drift, not Step A work. If the '
        'role is genuine, say so in the plan and add it to R04_PENDING_ROLES deliberately.'
    )
