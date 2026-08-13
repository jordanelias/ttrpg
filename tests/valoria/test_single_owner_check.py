#!/usr/bin/env python3
"""Guard for tools/single_owner_check.py (ED-IN-0180).

The tool reports modules that read a registry directly when a single owner already exists. Its
whole value rests on asking a FACTUAL question — *does this module build a path to the registry?* —
rather than looking for modules that claim ownership in a comment. So these tests attack the two
ways that question can go wrong: matching prose instead of code, and matching nothing at all.
"""
from __future__ import annotations

import os
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))

import single_owner_check as soc  # noqa: E402


@pytest.fixture(scope='module')
def found():
    return soc.find_bypasses()


def test_the_scan_reaches_a_real_corpus(found):
    """Assert that it asserted. A walk that finds nothing would make the ratchet vacuous."""
    assert set(found) == set(soc.OWNED), 'a registry vanished from the report'
    assert sum(len(v) for v in found.values()) > 0, (
        'zero bypasses found. Either the tree genuinely consolidated — in which case lower '
        'BASELINE to 0 in the same commit — or the AST walk stopped matching and this ratchet '
        'is now blind.')


def test_the_bypass_count_has_not_grown(found):
    """THE RATCHET. Report-only in the tool; here it is a real assertion because a NEW direct
    reader is a fresh violation of CLAUDE.md §8, not the pre-existing backlog."""
    total = sum(len(v) for v in found.values())
    assert total <= soc.BASELINE, (
        f'direct registry readers grew {soc.BASELINE} -> {total}. A new module started reading an '
        f'owned registry itself; route it through the owner. If this is deliberate, move the '
        f'BASELINE and say why in the same commit.')


def test_baseline_is_not_stale_low(found):
    """A baseline BELOW the truth would make the assertion above fail for everyone else's commit."""
    total = sum(len(v) for v in found.values())
    assert soc.BASELINE == total, (
        f'BASELINE is {soc.BASELINE} but the tree has {total}. Keep them equal — a ratchet that '
        f'is not tight measures nothing, and one set too low blocks unrelated work.')


def test_known_bypasses_are_actually_found(found):
    """The tool must see the bypasses the alias plan and ED-IN-0159 independently documented.

    These are named in `tools/pathres.py`'s own header as the four parsers it has not yet
    absorbed. If the scan stops seeing them it has broken, regardless of what total it reports.
    """
    alias = set(found['references/restructure_ledger.md'])
    for known in ('tools/broken_dependency_checker.py', 'tools/ci_claude_workflow_paths.py',
                  'skills/valoria-vector-audit/scripts/vector_audit.py',
                  'skills/valoria-vector-audit/scripts/workbench.py'):
        assert known in alias, f'{known} parses the alias ledger but was not reported'


def test_a_comment_mentioning_a_registry_is_NOT_a_bypass(tmp_path):
    """The defect the first version of this tool actually had.

    `build_engine_atlas.py` mentions `restructure_ledger.md` in a comment and does not parse it.
    A regex over file text reported it; the AST walk must not.
    """
    mod = tmp_path / 'prose_only.py'
    mod.write_text(
        '"""This module talks about references/restructure_ledger.md at length."""\n'
        '# see references/restructure_ledger.md for the alias map\n'
        'X = 1\n', encoding='utf-8')
    consts, _ = soc.module_reads(str(mod))
    assert not any('restructure_ledger.md' in c for c in consts), (
        'a docstring and a comment were counted as code touching the registry')


def test_a_real_path_build_IS_a_bypass(tmp_path):
    """The positive control. Without this, the test above only proves the tool finds nothing."""
    mod = tmp_path / 'real_reader.py'
    mod.write_text(
        'import os\n'
        'p = os.path.join("references", "restructure_ledger.md")\n', encoding='utf-8')
    consts, imports = soc.module_reads(str(mod))
    assert any('restructure_ledger.md' in c for c in consts), (
        'a genuine path build was missed — the scan cannot see what it exists to see')
    assert 'pathres' not in imports


def test_the_tool_does_not_count_itself(found):
    """It did, on its first run — reporting itself against all three registries because its OWNED
    table names them (ED-IN-0159 §2.4, recurring). Pinned so the exclusion cannot be dropped."""
    for registry, hits in found.items():
        assert 'tools/single_owner_check.py' not in hits, (
            f'the instrument counted itself under {registry}; the total is inflated by its own '
            f'configuration.')


def test_every_declared_owner_exists():
    """An owner that is not in the tree makes its whole row unfalsifiable."""
    for registry, spec in soc.OWNED.items():
        assert os.path.exists(os.path.join(ROOT, spec['owner'])), (
            f'{registry} names owner {spec["owner"]}, which does not exist')


def test_the_tool_is_report_only():
    """It reds on day one by design; `--check` must still exit 0 at the baseline."""
    assert soc.main(['--check']) == 0
