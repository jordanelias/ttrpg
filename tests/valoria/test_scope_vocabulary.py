"""The commit-scope vocabulary has ONE spelling, and this is the guard that says so (ED-IN-0119).

REPLACES A GUARD THAT HAD NOT RUN SINCE THE ORCHESTRATOR WAS RETIRED. `references/
scope_vocabulary.md` advertised, in its own header, a **"Drift guard: tests/hooks/
test_scope_vocabulary.py (asserts the three live sets match this doc; fails on any divergence)"**.
That test imported `valoria_hooks` and `github_ops` — retired modules absent from the live tree —
and `sys.path.insert(0, '/home/claude')`. It could not import, and no CI job or hook ran it anyway.

The claim was not merely stale, it was load-bearing and false: real drift accumulated behind it.
Measured 2026-08-01, `CLAUDE.md` §2 lists **12** commit scopes and the doc pinned **11** — `design`
was added to the live vocabulary and the drift guard did not notice, because there was no drift
guard. This is the same shape as the retired "CI-enforced index+infill" claim CLAUDE.md §4 corrects:
a convention propagating by imitation while the doc asserts an enforcement that does not exist.

WHAT CHANGED ABOUT THE SOURCE. The old test read the vocabulary out of the orchestrator's Python.
That owner is gone, so the live authority is `CLAUDE.md` §2, which is what commit messages are
actually written against. The two SESSION-scope and TASK-type axes the old test also covered were
sourced entirely from `github_ops`/`valoria_hooks` and retired with them; they are recorded in the
doc as historical rather than guarded here, because guarding a vocabulary nothing consumes would
be the dead-gate defect this file exists to correct.
"""
import os
import re

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
CLAUDE_MD = os.path.join(ROOT, 'CLAUDE.md')
VOCAB_DOC = os.path.join(ROOT, 'references', 'scope_vocabulary.md')


def _read(path):
    with open(path, encoding='utf-8') as fh:
        return fh.read()


def claude_md_scopes():
    """The live commit-scope set, from CLAUDE.md §2's `scope ∈ \\`a, b, c\\`` line."""
    m = re.search(r'scope ∈\s*\n?\s*`([^`]+)`', _read(CLAUDE_MD))
    assert m, ("CLAUDE.md §2 no longer states `scope ∈ \\`...\\`` — the commit-scope vocabulary has "
               "moved or been reworded. Repoint this guard rather than deleting it.")
    return {s.strip() for s in m.group(1).split(',') if s.strip()}


def doc_scopes():
    """The commit-scope set recorded in references/scope_vocabulary.md's table."""
    m = re.search(r'\*\*Commit scopes\*\*.*?\|\s*([a-z, ]+?)\s*\(\*\*(\d+)\*\*\)',
                  _read(VOCAB_DOC), re.S)
    assert m, "references/scope_vocabulary.md's Commit-scopes row is no longer parseable"
    return {s.strip() for s in m.group(1).split(',') if s.strip()}, int(m.group(2))


def test_both_sources_are_non_empty():
    """Guards the guard: an empty set on either side makes every comparison below vacuous —
    which is exactly how the predecessor managed to assert nothing at all."""
    live = claude_md_scopes()
    doc, _ = doc_scopes()
    assert len(live) >= 10, f'parsed only {len(live)} scope(s) from CLAUDE.md'
    assert len(doc) >= 10, f'parsed only {len(doc)} scope(s) from the vocabulary doc'


def test_the_doc_matches_claude_md():
    """THE DRIFT. `design` was live in CLAUDE.md and missing from the doc for an unknown period."""
    live = claude_md_scopes()
    doc, _ = doc_scopes()
    assert doc == live, (
        f'commit-scope vocabulary has drifted.\n'
        f'  in CLAUDE.md §2 but not the doc: {sorted(live - doc)}\n'
        f'  in the doc but not CLAUDE.md:    {sorted(doc - live)}\n'
        f'Update references/scope_vocabulary.md and CLAUDE.md §2 in the SAME commit — that '
        f'co-update requirement is the single-source enforcement this guard exists to provide.')


def test_the_docs_own_stated_count_matches_its_own_list():
    """The doc writes the count as a literal `(**11**)`. A list edited without the number is the
    cheapest possible way for this doc to start lying again."""
    doc, stated = doc_scopes()
    assert len(doc) == stated, f'doc lists {len(doc)} scopes but states (**{stated}**)'


def test_the_advertised_drift_guard_is_a_file_that_exists_and_runs():
    """The header claim that started this.

    Scoped to the `**Drift guard:**` LINE, not the whole document: the correction note below it
    names the retired path deliberately, as history. What must never come back is the *claim* that
    a non-existent file is enforcing something — so this asserts the advertised path resolves on
    disk and is under a root CI actually executes.
    """
    m = re.search(r'\*\*Drift guard:\*\*\s*`([^`]+)`', _read(VOCAB_DOC))
    assert m, 'references/scope_vocabulary.md no longer advertises a drift guard at all'
    advertised = m.group(1)
    assert os.path.isfile(os.path.join(ROOT, advertised)), (
        f'the doc advertises `{advertised}` as its drift guard, and that file does not exist. '
        f'This is the exact failure being corrected: an enforcement asserted in prose that cannot '
        f'run.')
    assert advertised.startswith(('tests/valoria/', 'engine/tests/', 'tests/contracts/')), (
        f'`{advertised}` is not under a pytest root CI executes, so advertising it as an enforcing '
        f'guard would be false again — just more subtly.')


@pytest.mark.parametrize('scope', ['infrastructure', 'fix', 'design', 'editorial'])
def test_scopes_this_repo_actually_commits_with_are_present(scope):
    """Anchors the set to observed practice, not just to two files agreeing with each other. Every
    scope here appears in real git history; `design` is the one the dead guard missed."""
    assert scope in claude_md_scopes()
