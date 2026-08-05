"""Canary corpus for `tools/pathres.py` — the path-resolution owner.

Each fixture below binds ONE branch of the owner to ONE historical defect. This is not general
coverage; it is a set of positive controls chosen so that crippling a branch resurrects a specific,
named failure that already happened in this repo:

| fixture                         | branch bound         | mutation it catches                     |
|---------------------------------|----------------------|-----------------------------------------|
| substring anchor                | `path_token_re`      | drop the lookbehind -> ED-IN-0133 phantom|
| split-path reconstruction       | `py_joined_paths`    | delete the join branch -> ED-IN-0128     |
| `params/core.md` alias          | dir-prefix resolve   | cripple prefixes -> the census-zero      |
| `references/params_core.md`     | chained resolve      | cap hops at 1 -> chain rot               |
| dead-but-prefix-mapped          | never-false-pass     | drop the existence check                 |
| indirection through a constant  | `py_path_io` env     | drop the env -> under-report by variable |

The last one is not a historical defect but a defect I caused and caught while building this: the
tracer initially saw 24 paths repo-wide because the dominant idiom binds a path to a module
constant and calls `open(NAME)`. A tracer that only sees inlined literals is a substring scan
wearing an AST.
"""
import os
import sys

import pytest

HERE = os.path.dirname(__file__)
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import pathres  # noqa: E402


# --------------------------------------------------------------------------------------
# Extraction: the anchor that stops a phantom directory being reported (ED-IN-0133)
# --------------------------------------------------------------------------------------

def test_a_tree_name_inside_a_longer_word_is_not_a_path_token():
    """THE ED-IN-0133 DEFECT, verbatim.

    `skills/valoria-vector-audit/scripts/vector_audit.py` contains the letters `audit/scripts/`.
    An unanchored scan for `audit/…` matched inside it and reported a directory that does not
    exist as a finding. The left lookbehind is the whole fix.
    """
    text = 'see skills/valoria-vector-audit/scripts/vector_audit.py for the run'
    refs = [r.raw for r in pathres.iter_path_refs(text)]
    assert not any(r.startswith('audit/') for r in refs), (
        f'a phantom audit/ token was extracted from a hyphenated word: {refs}')
    assert 'skills/valoria-vector-audit/scripts/vector_audit.py' in refs, \
        'the real reference on that line was lost — the anchor is too strong'


def test_a_real_reference_is_still_extracted():
    """Anti-vacuity: an anchor that rejects everything would pass the test above."""
    refs = [r.raw for r in pathres.iter_path_refs('reads audit/2026-06-03-x/engine.py at boot')]
    assert 'audit/2026-06-03-x/engine.py' in refs


def test_a_glob_is_captured_whole():
    """Truncating at the `*` yields a path that never exists and reports a false DEAD."""
    refs = [r.raw for r in pathres.iter_path_refs('paths: registers/editorial_ledger*.jsonl')]
    assert 'registers/editorial_ledger*.jsonl' in refs


# --------------------------------------------------------------------------------------
# Extraction: the split path a substring scan CANNOT see (ED-IN-0128)
# --------------------------------------------------------------------------------------

def test_a_constructed_path_is_reconstructed():
    """THE ED-IN-0128 DEFECT, verbatim: the parity-oracle load that no substring scan can see."""
    src = ("import os\n"
           "P = os.path.join(REPO_ROOT, 'audit', '2026-06-03-contest-groundup', 'engine.py')\n")
    assert 'audit/2026-06-03-contest-groundup/engine.py' in pathres.py_joined_paths(src)
    assert 'audit/' not in src, 'the fixture must not contain the literal — else it proves nothing'


def test_a_non_constant_segment_is_skipped_not_guessed():
    """Guessing a variable's value is the fabrication this repo forbids. A shorter path that still
    matches on its root is the correct degradation."""
    src = "import os\nP = os.path.join(REPO, 'audit', session_name, 'engine.py')\n"
    got = pathres.py_joined_paths(src)
    assert not any('session_name' in g for g in got), f'a variable name was baked into a path: {got}'


# --------------------------------------------------------------------------------------
# Resolution: the alias map — the defect that reported 0 of 58
# --------------------------------------------------------------------------------------

def test_the_relocated_params_path_resolves():
    """THE 2026-08-04 CENSUS DEFECT. `params/core.md` is how 46 provenance citations in kept code
    spell a file that lives at `engine/params/core.md`. A literal check scores them zero."""
    r = pathres.resolve('params/core.md')
    assert r.status == pathres.ALIASED, f'expected ALIASED, got {r}'
    assert r.live_path == 'engine/params/core.md'
    assert r.hops, 'a resolution through the map must record the hop it took'


def test_a_chained_alias_resolves():
    """The ledger contains a real two-hop chain. A single-hop resolver silently calls it dead."""
    r = pathres.resolve('references/params_core.md')
    assert r.status == pathres.ALIASED
    assert r.live_path == 'engine/params/core.md'
    assert len(r.hops) >= 2, f'expected a multi-hop chain, got {r.hops}'


def test_max_hops_one_reproduces_single_hop_behaviour():
    """`broken_dependency_checker` resolves one hop. Migrating it must be able to keep that
    exactly, or the refactor silently loosens a BLOCKING gate."""
    assert pathres.resolve('references/params_core.md', max_hops=1).status == pathres.DEAD


def test_a_prefix_that_maps_but_whose_target_is_absent_is_DEAD():
    """NEVER-FALSE-PASS. `designs/` maps to `audit/`, but the file does not exist at either end.
    Dropping the existence check would report every mapped-prefix path as resolved."""
    r = pathres.resolve('designs/audit/definitely-not-here.md')
    assert r.status == pathres.DEAD
    assert r.live_path is None


def test_a_live_path_needs_no_alias():
    r = pathres.resolve('engine/substrate/keys.py')
    assert r.status == pathres.LIVE and r.live_path == 'engine/substrate/keys.py' and not r.hops


def test_glob_resolution_does_not_use_the_exists_path():
    """`resolve()` tests os.path.exists, always False for a pattern — a legitimate glob would
    report a false DEAD."""
    assert pathres.resolve_glob('registers/editorial_ledger*.jsonl').status == pathres.LIVE


# --------------------------------------------------------------------------------------
# The return type: making the wrong question visibly wrong
# --------------------------------------------------------------------------------------

def test_a_resolution_is_not_a_string():
    """All three defects were a silent substitution of the question. A Resolution that compares
    equal to a path, or stringifies to one, lets the substitution stay invisible."""
    r = pathres.resolve('params/core.md')
    assert r != 'engine/params/core.md', 'Resolution compares equal to a raw path'
    assert 'engine/params/core.md' not in str(r).split("'")[0], 'str(Resolution) yields a bare path'
    assert r.live_path == 'engine/params/core.md', 'the explicit question must still be answerable'


def test_a_resolution_has_no_truth_value():
    """`if resolve(x):` is the question-hiding shortcut. It must raise, not silently mean
    something."""
    with pytest.raises(TypeError):
        bool(pathres.resolve('params/core.md'))


def test_same_file_resolves_both_sides():
    assert pathres.resolve('params/core.md').same_file('engine/params/core.md')
    assert not pathres.resolve('params/core.md').same_file('engine/substrate/keys.py')


# --------------------------------------------------------------------------------------
# I/O tracing: a mention is not a dependency
# --------------------------------------------------------------------------------------

@pytest.mark.parametrize('src,expected', [
    ("open('references/x.yaml')", ('references/x.yaml', 'read')),
    ("open('references/x.yaml', 'w')", ('references/x.yaml', 'write')),
    ("open('references/x.yaml', 'a')", ('references/x.yaml', 'write')),
    ("open('references/x.yaml', mode='w')", ('references/x.yaml', 'write')),
    ("import glob\nglob.glob('audit/**/*.md')", ('audit/**/*.md', 'scan')),
    ("import os\nos.remove('registers/old.jsonl')", ('registers/old.jsonl', 'delete')),
])
def test_io_mode_is_classified(src, expected):
    got = [(io.path, io.mode) for io in pathres.py_path_io(src)]
    assert expected in got, f'expected {expected} in {got}'


def test_a_mention_is_not_traced_as_io():
    """The distinction the whole tracer exists for: `evacuation_plan.readers()` calls any file
    naming an evacuating path a 'blocking reader', which is why one 43-file slice reported 30 of
    them, mostly comments. A comment breaks nothing when the file goes."""
    src = "# see references/x.yaml for the schema\nVALUE = 3\n"
    assert pathres.py_path_io(src) == []


def test_io_through_a_module_constant_is_traced():
    """THE DEFECT I CAUSED BUILDING THIS. Without a constant environment the tracer saw 24 paths
    in the entire repo, because the dominant idiom is bind-then-open. A tracer blind to one level
    of indirection is the same under-report as a literal path scan."""
    src = ("import os\n"
           "ROOT = '/x'\n"
           "LEDGER = os.path.join(ROOT, 'references', 'restructure_ledger.md')\n"
           "def f():\n"
           "    return open(LEDGER).read()\n")
    got = [(io.path, io.mode) for io in pathres.py_path_io(src)]
    assert ('references/restructure_ledger.md', 'read') in got, \
        f'I/O through a module constant was not traced: {got}'


def test_the_io_tracer_is_not_vacuous():
    """A tracer returning [] for everything would satisfy the mention test above.

    Exemplar chosen by MEASUREMENT, not assumption: the first draft of this test used
    `evacuation_plan.py` and failed, which is correct behaviour and is recorded as the blind-spot
    test below — that tool opens `os.path.join(REPO, rel)` where `rel` is a loop variable, so
    there is nothing constant to trace. The floor is deliberately low (>= 1) because the honest
    coverage of this tracer IS low; a high floor here would be a claim the tracer cannot support.
    """
    with open(os.path.join(ROOT, 'tools', 'ci_claude_workflow_paths.py'), encoding='utf-8') as fh:
        traced = pathres.py_path_io(fh.read())
    assert traced, 'the I/O tracer found nothing in a tool that opens a constant-bound path'


def test_the_known_blind_spot_is_a_blind_spot_and_is_recorded():
    """DYNAMIC PATHS ARE INVISIBLE, and pretending otherwise is how a partial tool gets trusted
    as a complete one.

    `open(os.path.join(REPO, rel))` for a loop variable `rel` cannot be resolved without dataflow
    analysis, and guessing is the fabrication this repo forbids. So the tracer returns nothing for
    it — which means **`pathres pipeline` is a candidate-finder, not a census**, and any count it
    produces is a LOWER BOUND. This test exists so that statement is enforced rather than
    remembered: if a future change makes this pass, the docstrings claiming a lower bound are
    wrong and must be updated with it.
    """
    src = ("import os\n"
           "for rel in files:\n"
           "    open(os.path.join(REPO, rel)).read()\n")
    assert pathres.py_path_io(src) == [], (
        'the tracer now resolves a dynamic path — good, but `pipeline`\'s "lower bound" caveat '
        'in tools/pathres.py and HANDOFF_IN.md is now stale and must be corrected')


# --------------------------------------------------------------------------------------
# The map itself
# --------------------------------------------------------------------------------------

def test_the_alias_map_is_not_empty():
    """Every resolve() degrades to DEAD if the ledger stops parsing. That failure must be loud."""
    exact, prefix = pathres.load_alias_map()
    assert len(exact) > 100, f'only {len(exact)} exact alias rows parsed — the ledger regex broke'
    assert len(prefix) >= 10, f'only {len(prefix)} dir-prefix rows parsed'
