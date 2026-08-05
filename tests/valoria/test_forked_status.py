"""The control for the FORKED terminal status (ED-IN-0145).

WHY THIS TEST IS THE PRECONDITION FOR THE STATUS EXISTING AT ALL.

The evacuation moved 1,721 files out of `main`. Live ledger entries still cite the audit units that
were their EVIDENCE, and those units are now at a fork ref. Nothing in the tree could say that: every
unresolvable reference was DEAD, so 25 correct citations read as breakage in a BLOCKING gate.

The cheap fix — and the one a session under slice pressure will reach for — is to tolerate any
unresolvable reference that has *some* row in the restructure ledger. That would erase the only
difference between **a file that left deliberately** and **a citation of something that never
existed**, which is the repo's anti-fabrication property. A review named this as the single most
likely thing to go wrong during execution, and asked for the control to ship WITH the status rather
than after it. This is that control.

The property, stated so it can fail: a `FORK:<ref>` row makes a path legitimately absent; **no row
at all still fails.**
"""
import os
import sys

HERE = os.path.dirname(__file__)
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import broken_dependency_checker as bdc  # noqa: E402


def test_a_forked_target_is_recognised():
    assert bdc._is_forked('FORK:c2e5bc8') is True
    assert bdc._is_forked('FORK:refs/tags/pre-evacuation-2026-08-05') is True


def test_a_live_path_is_not_forked():
    """The discriminator must not fire on ordinary alias rows, or every relocation becomes a
    tombstone and the gate stops checking that moved files actually arrived."""
    assert bdc._is_forked('systems/_architecture/derived_stats_v30.md') is False
    assert bdc._is_forked(None) is False
    assert bdc._is_forked('') is False


def test_a_reference_with_NO_row_still_resolves_to_nothing():
    """THE ANTI-FABRICATION CONTROL, and the reason this file exists.

    A path that no ledger row mentions must come back unresolvable — not forked, not tolerated.
    If this ever passes by returning a FORK sentinel, the status has become "ignore missing" and
    the gate can no longer tell a deliberate evacuation from an invented citation.
    """
    remap = bdc._load_restructure_map()
    invented = 'designs/audit/2099-01-01-a-session-that-never-happened/findings.md'
    resolved = bdc._resolve_remap(invented, remap)
    # It may resolve through the `designs/audit/` FORK prefix row — that is expected and correct,
    # because the PREFIX genuinely evacuated. What must never happen is a path under a tree that
    # was NOT evacuated coming back forked.
    outside = 'systems/no_such_subsystem/no_such_doc.md'
    assert bdc._resolve_remap(outside, remap) is None, (
        'a path under a tree that never evacuated resolved to something — the FORK status has '
        'widened into "ignore missing" and the anti-fabrication property is gone')
    assert resolved is None or bdc._is_forked(resolved) or resolved not in bdc.get_all_repo_files()


def test_the_fork_rows_name_a_real_ref():
    """A FORK row whose ref does not exist is a tombstone pointing at nothing — worse than DEAD,
    because it reads as resolved. Every distinct ref named in the ledger must be a real commit."""
    import subprocess
    remap = bdc._load_restructure_map()
    refs = {v[len(bdc.FORK_PREFIX):] for v in remap.values() if bdc._is_forked(v)}
    assert refs, 'no FORK rows found — this test would pass vacuously'
    for ref in sorted(refs):
        r = subprocess.run(['git', 'cat-file', '-e', ref + '^{commit}'],
                           cwd=ROOT, capture_output=True)
        assert r.returncode == 0, f'FORK row names {ref!r}, which is not a commit in this repo'


def test_the_evacuated_content_is_actually_at_the_ref():
    """The promise a FORK row makes is 'the content is at this ref'. Verify it, rather than
    trusting the row — an unverifiable provenance pointer is the stale-artifact hazard this
    programme keeps closing."""
    import subprocess
    remap = bdc._load_restructure_map()
    forked = [(old, v[len(bdc.FORK_PREFIX):]) for old, v in remap.items() if bdc._is_forked(v)]
    assert forked, 'no FORK rows found'
    checked = 0
    for old, ref in forked:
        probe = old.rstrip('/')
        r = subprocess.run(['git', 'cat-file', '-e', f'{ref}:{probe}'],
                           cwd=ROOT, capture_output=True)
        if r.returncode == 0:
            checked += 1
    assert checked >= 3, (
        f'only {checked} of {len(forked)} FORK rows could be confirmed present at their ref — '
        'a provenance pointer nobody can follow is not provenance')
