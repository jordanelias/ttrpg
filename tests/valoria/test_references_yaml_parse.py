"""Every machine-read YAML register must actually parse (ED-IN-0121).

`references/npc_registry.yaml` was unparseable for the whole of its visible git history and
NOTHING NOTICED. A `faction:` value contained an unquoted colon —

    faction: Church (dual-loyalty: Crown Inner Circle agent for Himlensendt)

— which YAML reads as a nested mapping key, so `yaml.safe_load` raised `ScannerError` at line 480.
It survived because the file has zero Python loaders: its only two "references" are a path-prefix
tuple in `audit_staleness.py` and a comment. A register nobody loads cannot report that it is
broken, and no gate in the apparatus parsed `references/*.yaml` at all.

That is the same shape as every defect this session repaired — a surface asserted to be machine-read
that nothing machine-reads — and it is the cheapest possible guard to add: 31 files, one
`safe_load` each, ~40 ms. Measured at introduction: exactly ONE file failed, so this lands green
after a one-line quoting repair rather than importing a backlog into a gate (CLAUDE.md §0.1 point 5
on the cost of widening scope).

Deliberately NOT asserting schema, keys or content — only that the bytes are loadable. A parse gate
that grew opinions about structure would start failing on legitimate edits and get switched off.
"""
import glob
import os

import pytest

yaml = pytest.importorskip('yaml')

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

# The machine-read register trees. `deprecated/` is excluded on purpose: it is frozen history, and
# a retired file that no longer parses is not a defect anyone should be made to fix.
TREES = ('references/**/*.yaml', 'references/**/*.yml', 'registers/*.yaml', 'registers/*.yml')


def _register_files():
    out = []
    for pat in TREES:
        out += glob.glob(os.path.join(ROOT, pat), recursive=True)
    return sorted(set(out))


def test_there_are_registers_to_check():
    """Guards the guard: an empty file list makes the parametrized test below vacuous, which is
    precisely the failure mode this module exists to catch in others."""
    files = _register_files()
    assert len(files) > 20, f'only {len(files)} register file(s) found — the globs are broken'


@pytest.mark.parametrize('path', _register_files(), ids=lambda p: os.path.relpath(p, ROOT))
def test_every_register_parses(path):
    rel = os.path.relpath(path, ROOT)
    with open(path, encoding='utf-8') as fh:
        try:
            yaml.safe_load(fh)
        except yaml.YAMLError as exc:
            mark = getattr(exc, 'problem_mark', None)
            where = f' at line {mark.line + 1}, column {mark.column + 1}' if mark else ''
            pytest.fail(
                f'{rel} is not loadable YAML{where}: {getattr(exc, "problem", exc)}.\n'
                f'A register that cannot be parsed is not a register. The usual cause is an '
                f'unquoted colon inside a scalar — wrap the value in quotes; that changes the '
                f'YAML escaping and not the string.')
