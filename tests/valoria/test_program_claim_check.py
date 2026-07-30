"""Guard for tools/ci_program_claim_check.py (ED-IN-0098).

The tool's whole justification is one historical incident, so the primary test REPLAYS that
incident: W4 (ED-IN-0097) retired `tools/registry.py` while
`audit/2026-07-29-centralization-single-owner/` held a declared claim on it, and nothing stopped
the sweep because the interlock was prose. If the tool cannot detect that exact diff against the
live tree, it does not do the one job it was written for.

That test is deliberately coupled to real repo content (CSO's pointer). If the CSO program
completes and its pointer stops being LIVE, this test SHOULD fail — at which point replace the
replay fixture with a synthetic one and say so, rather than deleting the coverage.
"""
import os
import sys

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import ci_program_claim_check as c  # noqa: E402


def test_replays_the_registry_py_incident():
    """THE regression: the W4 retirement diff must be flagged, naming CSO as claimant."""
    claims = c.load_claims()
    hits = c.overlaps(['tools/registry.py'], claims)
    assert hits, (
        'tools/registry.py is not detected as claimed. Either CSO\'s pointer stopped being LIVE '
        '(then re-point this test at a synthetic fixture and say so), or the claim parser broke — '
        'in which case the tool no longer does the one thing it exists for.')
    claimants = {pointer for _f, pointer, _claimed in hits}
    assert any('centralization_single_owner' in p for p in claimants), (
        f'expected the centralization-single-owner pointer as claimant, got {claimants}')


def test_self_filter_suppresses_your_own_program():
    """A session must be able to exclude its own claims, or the signal is pure noise."""
    all_claims = c.load_claims()
    filtered = c.load_claims(self_filter='centralization_single_owner')
    assert any('centralization_single_owner' in k for k in all_claims)
    assert not any('centralization_single_owner' in k for k in filtered)


def test_only_live_pointers_contribute_claims():
    """A retired/absorbed program must not veto changes. Parse liveness, don't assume it."""
    live, verdict = c._is_live('**liveness:** LIVE — executed by a dedicated session')
    assert live is True and 'LIVE' in verdict
    live_partial, _ = c._is_live('**liveness:** **LIVE-PARTIAL** — Status: PROPOSED')
    assert live_partial is True, 'LIVE-PARTIAL still holds claims'
    dead, _ = c._is_live('**liveness:** ABSORBED into the 2026-07-29 program; historical only')
    assert dead is False
    none, why = c._is_live('no liveness line here')
    assert none is False and 'no liveness' in why


def test_prose_backticks_are_not_mistaken_for_paths():
    """`resolve()` and `ED-IN-0091` are not files. A claim parser that thinks so is unusable."""
    text = ('**scope:** Completion of the `resolve()`/`all_known()` facade per `ED-IN-0091`, '
            'touching `tools/registry.py` and `references/module_contracts.yaml`.\n')
    paths = c._claimed_paths(text)
    assert paths == {'tools/registry.py', 'references/module_contracts.yaml'}, paths


def test_directory_claim_covers_files_beneath_it():
    """A claim on `systems/combat/` must cover a file inside it, or seam claims are useless."""
    claims = {'P.md': {'systems/combat/'}}
    hits = c.overlaps(['systems/combat/combat_engine_v1/wrapper.py'], claims)
    assert hits and hits[0][1] == 'P.md'


def test_no_overlap_returns_cleanly():
    claims = {'P.md': {'tools/registry.py'}}
    assert c.overlaps(['README.md', 'tools/ci_common.py'], claims) == []


def test_tool_runs_and_is_report_only():
    """Exit code must be 0 even with overlaps — promoting to blocking is Jordan's call."""
    assert c.main(['--base', 'HEAD']) == 0
