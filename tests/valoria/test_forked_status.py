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
    assert bdc._is_forked('FORK:c451bcb') is True
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
    """The promise a FORK row makes is "the content is at this ref". Verify EVERY row, and pin the
    number that cannot be verified so it can only shrink.

    REWRITTEN 2026-08-21 (ED-IN-0194) after this test failed to catch the exact defect it exists
    for. It counted rows it COULD confirm and asserted `checked >= 3` against ~200 rows — so 229
    rows could point at nothing and it still passed. A culling pass then added 77 rows naming
    `3be53ef`, the commit that PERFORMS the deletion: a file deleted BY a commit is not present AT
    it, so all 77 were unfollowable from the moment they were written, and this test was green.

    That is CLAUDE.md §0.1 pt 2 verbatim — an assertion that cannot observe the failure it excludes
    — committed inside a provenance guard, which is the worst possible host for it. The floor was
    measuring the test's own reach, not the ledger's health.

    Now it counts the rows that CANNOT be followed and ratchets that number down. A hard zero would
    be red on arrival: 79 pre-existing rows name `designs/`-era paths at refs where those paths had
    already moved, which is inherited debt and not this test's to fix in one commit. A ceiling that
    only falls is the honest shape — the same one `test_engine_does_not_import_systems.py` uses.
    """
    import subprocess
    remap = bdc._load_restructure_map()
    forked = [(old, v[len(bdc.FORK_PREFIX):]) for old, v in remap.items() if bdc._is_forked(v)]
    assert forked, 'no FORK rows found — this test would pass vacuously'

    unresolvable = []
    for old, ref in forked:
        probe = old.rstrip('/')
        r = subprocess.run(['git', 'cat-file', '-e', f'{ref}:{probe}'],
                           cwd=ROOT, capture_output=True)
        if r.returncode != 0:
            unresolvable.append(f'{old} -> {ref}')

    # THE CEILING. Re-measured 2026-08-21 after an adversarial pass falsified the first figure's
    # PROVENANCE (not its arithmetic): it said "79 of 232, all of them pre-existing `designs/`-era
    # rows", and the ledger holds only 77 `designs/` rows — so at least two were something else,
    # and the sentence "every row added since is verified reachable" was false because one of them
    # was `workplans/POINTER_*.md`, a GLOB row this session had added. A glob cannot be verified by
    # `git cat-file -e <ref>:<path>` — no shell expansion — so it was unfollowable by construction
    # inside a block claimed as row-by-row verified. Replaced with its 11 real filenames.
    #
    # TRUE COMPOSITION, measured with the same command this test uses: 78 of 242 unfollowable —
    # 77 pre-existing `designs/`-era rows, plus `references/values_master.yaml -> c451bcb`, which
    # is also inherited (that file moved to `deprecated/references/` on 2026-08-02, three days
    # before `c451bcb` was cut). ZERO come from this session: all 86 of its rows resolve.
    UNRESOLVABLE_CEILING = 78

    assert len(unresolvable) <= UNRESOLVABLE_CEILING, (
        f'FORK rows that cannot be followed ROSE {UNRESOLVABLE_CEILING} -> {len(unresolvable)}. '
        f'A provenance pointer nobody can follow is not provenance — it is worse than a DEAD row, '
        f'because it reads as resolved. All offenders (the {UNRESOLVABLE_CEILING} inherited ones '
        f'plus whatever this change added — the new one is the row you just touched):\n  '
        + '\n  '.join(unresolvable)[:1200] + '\n'
        f'Verify a row with `git cat-file -e <ref>:<path>` BEFORE writing it. If you are recording '
        f'a deletion, the content is at the PARENT of the deleting commit, not at it.')

    assert len(unresolvable) == UNRESOLVABLE_CEILING, (
        f'FORK rows that cannot be followed FELL {UNRESOLVABLE_CEILING} -> {len(unresolvable)}. '
        f'Lower UNRESOLVABLE_CEILING to {len(unresolvable)} in this commit so the progress is banked.')

    # And the assertion that the loop ran at all (§0.1 pt 2) — the property whose absence is the
    # reason this test was rewritten. Counting failures, not successes, means a scan that stops
    # working reports ZERO problems; this makes that indistinguishable-from-healthy state fail.
    assert len(forked) >= 200, (
        f'only {len(forked)} FORK rows parsed (expected 200+) — the ledger reader has stopped '
        f'matching rows, so the count above is measuring nothing. Fix the parser, not this floor.')
