"""The `.md` sweep guard is a MECHANISM, not a rule — so it needs a test, not a paragraph.

Jordan, 2026-08-24: *"unless I specifically mention prose or documents, I do not want any .md
documents scanned"*, and one instruction earlier, *"whatever mechanisms we have that rely on prose
are worthless."* A CLAUDE.md paragraph telling the agent not to sweep markdown is prose, and prose
was just demoted. `.claude/settings.json` runs `tools/hook_md_sweep_guard.py` on every Grep/Glob;
this pins that it is wired and that it discriminates.
"""
import json
import os
import sys

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import hook_md_sweep_guard as guard  # noqa: E402


def test_the_guard_is_wired_into_the_harness():
    """A guard nobody invokes is a file, not a mechanism."""
    cfg = json.load(open(os.path.join(ROOT, '.claude', 'settings.json'), encoding='utf-8'))
    cmds = [h.get('command', '')
            for m in cfg.get('hooks', {}).get('PreToolUse', []) for h in m.get('hooks', [])]
    assert any('hook_md_sweep_guard.py' in c for c in cmds), \
        'the md-sweep guard is not wired into PreToolUse — it cannot fire'
    matchers = [m.get('matcher', '') for m in cfg['hooks']['PreToolUse']
                if any('hook_md_sweep_guard' in h.get('command', '') for h in m.get('hooks', []))]
    assert any('Grep' in m and 'Glob' in m for m in matchers), \
        f'guard is wired but not to Grep|Glob: {matchers}'


@pytest.mark.parametrize('tool,ti,blocked,why', [
    ('Glob', {'pattern': '**/*.md'}, True, 'the broad sweep this exists to stop'),
    ('Glob', {'pattern': 'systems/**/*.md'}, True, 'a whole-subsystem doc sweep'),
    ('Grep', {'pattern': 'Conviction', 'glob': '*.md'}, True, 'grep restricted to markdown'),
    ('Grep', {'pattern': 'Conviction'}, True, 'unscoped grep rakes the tree'),
    ('Grep', {'pattern': 'CONVICTIONS', 'path': 'systems/', 'glob': '**/*.py'}, False, 'code search'),
    ('Glob', {'pattern': 'engine/**/*.py'}, False, 'code glob'),
    ('Read', {'file_path': 'systems/combat/combat_v30.md'}, False, 'naming a file IS explicit'),
    ('Edit', {'file_path': 'x.md'}, False, 'editing is not sweeping'),
])
def test_it_blocks_sweeps_and_permits_deliberate_reads(tool, ti, blocked, why):
    got, _ = guard.verdict(tool, ti)
    assert got is blocked, f'{tool} {ti} -> blocked={got}, expected {blocked} ({why})'


def test_markdown_that_CODE_reads_is_never_blocked():
    """THE CARVE-OUT THAT MATTERS. Some `.md` are inputs, not reference — the Key-bus schema
    among them. A guard that blocked those would break real work, so the allowlist is DERIVED
    from code rather than hardcoded, and this proves the derivation reaches the important ones."""
    allow = guard._machine_read_md()
    assert allow, 'the machine-read markdown set came back empty — the derivation is broken'
    assert 'key_type_registry_v30.md' in allow, \
        'the Key-type schema is authored in markdown and MUST stay searchable'
    for name in ('key_type_registry_v30.md', 'restructure_ledger.md'):
        got, _ = guard.verdict('Grep', {'pattern': 'x', 'glob': name})
        assert got is False, f'{name} is a code input and must not be blocked'


def test_it_fails_OPEN_when_its_own_helper_breaks(monkeypatch):
    """A guard that blocks everything when its helper dies is worse than the drift it prevents."""
    monkeypatch.setattr(guard, '_machine_read_md', lambda: None)
    got, _ = guard.verdict('Glob', {'pattern': '**/*.md'})
    assert got is False, 'the guard failed CLOSED — it must fail open'


def test_the_escape_hatch_works(monkeypatch):
    """The ruling carves out prose work explicitly; the hatch must be real and explicit."""
    monkeypatch.setenv('VALORIA_ALLOW_MD_SWEEP', '1')
    got, _ = guard.verdict('Glob', {'pattern': '**/*.md'})
    assert got is False, 'VALORIA_ALLOW_MD_SWEEP=1 did not permit a deliberate prose sweep'
