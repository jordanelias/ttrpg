"""The EXPECTED-DELTA test for plan step G7 (ED-IN-0159 §8.1).

WHY THIS FILE EXISTS.

`audit/2026-08-11-code-leanness/01_plan.md` G7 collapses six primitives that were
re-implemented across `tools/` — the repo root (53 sites, 15 spellings), YAML
register load (44), the 9-lane roster (8), `id_reservations` read (8), token
estimation (6) and the PP/ED id regex (6) — onto one owner in `tools/ci_common.py`.

Every one of those copies AGREES today. That is the whole basis on which the plan
calls the migration mechanical, and CLAUDE.md §8 already ruled that each such
migration ships its own expected-delta test. §6 item 9 of the findings document is
blunt about the status of the claim without one:

    "Every Track-G 'expected delta: none' claim — these are predictions. Each is
     exactly what its own migration test must establish."

So this file does not assert that the new owner is *self-consistent*, which would
be vacuous (CLAUDE.md §0.1 point 2: an assertion must be able to observe the
failure it excludes). It recomputes each primitive **the way the call sites used to
compute it**, transcribed from their pre-migration sources, and asserts the owner
agrees. If a future edit changes `ci_common.REPO`'s spelling, `tokens()`'s
denominator or the lane tuple, these fail — which is the recurrence guard §0.1
point 5 asks for.

The transcriptions below are deliberately verbatim-ugly. Normalising them would
test the owner against itself.
"""
import ast
import os
import re
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))

import ci_common  # noqa: E402


# ── the repo root: all 15 spellings resolve to the one owner ─────────────────

def test_repo_root_matches_every_pre_migration_spelling():
    """§1.3b measured 15 distinct spellings across 53 sites. Every one of them
    computed the same directory; this asserts the owner did not move it.

    Each lambda is the expression as it appeared in a migrated module, evaluated
    with `__file__` bound to a file in `tools/` (the layer every one of them was
    written at). `tools/observability/` sits one level deeper and is covered
    separately below.
    """
    tools_file = os.path.join(ROOT, 'tools', 'ci_common.py')

    spellings = {
        # the dominant one — 24 sites
        'dirname(dirname(abspath))':
            os.path.dirname(os.path.dirname(os.path.abspath(tools_file))),
        # 4 sites
        "abspath(join(dirname, '..'))":
            os.path.abspath(os.path.join(os.path.dirname(tools_file), '..')),
        # 5 sites
        "abspath(join(dirname(abspath), '..'))":
            os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(tools_file)), '..')),
        # 6 sites (Path idiom)
        'Path(__file__).resolve().parents[1]':
            str(Path(tools_file).resolve().parents[1]),
    }
    for name, computed in spellings.items():
        assert computed == ci_common.REPO, f'spelling {name!r} no longer agrees with ci_common.REPO'


def test_repo_root_from_the_observability_layer():
    """`tools/observability/*` used `Path(__file__).resolve().parents[2]`."""
    obs_file = os.path.join(ROOT, 'tools', 'observability', 'obs_core.py')
    assert str(Path(obs_file).resolve().parents[2]) == ci_common.REPO


def test_repo_root_is_the_git_toplevel():
    """The independent check: git's own answer, which no spelling above consults.

    This is the one assertion here that could catch ALL fifteen spellings being
    wrong together — the failure mode a transcription test cannot see by
    construction.
    """
    top = subprocess.run(['git', 'rev-parse', '--show-toplevel'],
                         cwd=ROOT, capture_output=True, text=True)
    if top.returncode != 0:
        pytest.skip('not a git checkout')
    assert os.path.realpath(top.stdout.strip()) == os.path.realpath(ci_common.REPO)


def test_repo_path_is_derived_not_duplicated():
    """REPO and REPO_PATH are one definition in two shapes. If they ever differ,
    a call site's choice of idiom would change which tree it reads."""
    assert isinstance(ci_common.REPO, str)
    assert isinstance(ci_common.REPO_PATH, Path)
    assert str(ci_common.REPO_PATH) == ci_common.REPO
    assert ci_common._REPO == ci_common.REPO      # pre-G7 private alias


def test_repo_root_actually_points_at_this_repo():
    """A spelling that resolved one level too high would still be self-consistent
    above. Anchor it to files that exist only at the real root."""
    for marker in ('CLAUDE.md', 'CURRENT.md', 'pytest.ini'):
        assert os.path.isfile(os.path.join(ci_common.REPO, marker)), marker


# ── the 9-lane roster ────────────────────────────────────────────────────────

def test_lane_roster_matches_the_pre_migration_literals():
    """Transcribed verbatim from ci_workplan_pointer_check:52,
    broken_dependency_checker:171, handoff_atomize:37, validate_ed_citations:50,
    currency_consistency_check:122 — all five carried this literal."""
    assert ci_common.LANE_CODES == ("MB", "PC", "FI", "SC", "FA", "WR", "IN", "GO", "SE")
    assert ci_common.LEDGER_LANE_CODES == ('mb', 'pc', 'fi', 'sc', 'fa', 'wr', 'in', 'go', 'se')


def test_lane_roster_includes_go():
    """The specific failure on the record: obs_core's header notes that a prior
    roster silently OMITTED 'GO', undercounting a whole lane. A membership
    assertion, not a length one — a nine-element tuple with the wrong ninth
    element passes a length check."""
    assert 'GO' in ci_common.LANE_CODES


def test_lane_roster_matches_claude_md():
    """CLAUDE.md §4 is the prose owner of the taxonomy. If a tenth lane is added
    there and not here, the tools stop seeing it — which is the edit-surface
    problem G7 exists to close, now reduced to this one assertion."""
    text = (Path(ci_common.REPO) / 'CLAUDE.md').read_text(encoding='utf-8')
    # Backticks are required, not optional: CLAUDE.md §4 writes the roster as
    # "`MB` mass battle, `PC` personal combat, …". Without them this matched
    # "IP world-tracks" in the §3 `sim/peninsular/` row and reported a phantom
    # tenth lane — a false positive the first run of this test actually produced.
    declared = set(re.findall(r'`([A-Z]{2})` (?:mass battle|personal combat|'
                              r'field investigation|social contest|faction actions|'
                              r'world|infrastructure/cross-cutting|godot|settlements)', text))
    assert declared, 'CLAUDE.md §4 lane table not found — update this test, not the roster'
    assert len(declared) == 9, f'CLAUDE.md §4 declares {len(declared)} lanes: {sorted(declared)}'
    assert declared <= set(ci_common.LANE_CODES), f'lanes in CLAUDE.md missing from roster: {declared - set(ci_common.LANE_CODES)}'


def test_obs_core_re_exports_the_same_roster_object():
    """obs_core kept its LANE_CODES name for its 9 consumers. If it ever stopped
    being the SAME object, the divergence this step closed would be back."""
    sys.path.insert(0, os.path.join(ROOT, 'tools', 'observability'))
    import obs_core
    assert obs_core.LANE_CODES is ci_common.LANE_CODES
    assert obs_core.LEDGER_LANE_CODES is ci_common.LEDGER_LANE_CODES
    assert str(obs_core.REPO) == ci_common.REPO


# ── token estimation ─────────────────────────────────────────────────────────

@pytest.mark.parametrize('text', ['', 'a', 'abc', 'abcd', 'x' * 4001, 'é' * 100])
def test_tokens_matches_the_inline_len_div_4(text):
    """Every migrated site computed `len(content) // 4` inline:
    compliance_check:128,169,198,269,281 · ci_register_size_check:164 ·
    ci_hooks_verifier:73 · atomizer:265,312,558 · doc_index_gen:28,52 ·
    index_gen:261 · handoff_atomize:84.

    This is the denominator every size cap in the repo is written in, so a
    changed estimator silently re-scales `atomization_rules.yaml`.
    """
    assert ci_common.tokens(text) == len(text) // 4


def test_tokens_treats_missing_content_as_zero():
    """The one deliberate addition over the inline form: a size sweep over a tree
    where a file is absent should report 0, not raise. Stated so it is a decision
    rather than an accident."""
    assert ci_common.tokens(None) == 0


# ── id regexes ───────────────────────────────────────────────────────────────

def test_pp_id_pattern_is_a_composable_string_with_real_callers():
    """The ONLY id pattern exported, and the reason it is a string.

    Every migrated site embeds it in a larger expression — `ci_vetting_check.py`
    twice (a BLOCKING gate) and `export_sim_params.py` once — which a compiled
    object cannot do. The six compiled/narrow variants originally shipped beside it
    had ZERO callers and were removed; see the owner's comment.
    """
    assert isinstance(ci_common.PP_ID_PAT, str)
    assert re.compile(r'-\s+id:\s+' + ci_common.PP_ID_PAT).search('- id: PP-674')
    assert re.compile(ci_common.PP_ID_PAT).findall('PP-674 and PP-1') == ['PP-674', 'PP-1']


def test_pp_pattern_migration_is_delta_none_on_the_live_register():
    """Expected delta for the two `ci_vetting_check` sites, measured against the
    register they actually parse rather than against a synthetic string."""
    text = (Path(ci_common.REPO) / 'registers' / 'patch_register_active.yaml').read_text(
        encoding='utf-8')
    old_block = re.compile(r'-\s+id:\s+PP-(\d+)\s*\n(.*?)(?=\n-\s+id:\s+PP-\d+|\Z)', re.S)
    new_block = re.compile(
        r'-\s+id:\s+PP-(\d+)\s*\n(.*?)(?=\n-\s+id:\s+' + ci_common.PP_ID_PAT + r'|\Z)', re.S)
    assert old_block.findall(text) == new_block.findall(text)
    assert len(re.findall(r'-\s+id:\s+PP-\d+', text)) == \
        len(re.findall(r'-\s+id:\s+' + ci_common.PP_ID_PAT, text))


def test_the_two_live_ed_readers_are_deliberately_not_collapsed():
    """A NON-consolidation, asserted so it cannot be "tidied" later.

    `validate_ed_citations` matches flat `ED-\d+` ONLY BY DESIGN — the archives it
    salvages predate the lane-tagged format — while `ci_claim_provenance_check`
    parses `^(ED-[A-Z]+)-(\d+)$` into two capture groups. Same-looking, different
    meanings. Merging them is §8.2's "two concepts with one name", which the
    mission forbids; this test is the record of that decision.
    """
    assert not hasattr(ci_common, 'ED_ID_PAT'), (
        'an ED pattern was exported — check first that the two live readers really '
        'do mean the same thing, because today they do not')
    vec = (Path(ci_common.REPO) / 'tools' / 'validate_ed_citations.py').read_text(encoding='utf-8')
    assert r'(ED-\d+)' in vec, 'validate_ed_citations no longer flat-only — re-open the question'


# ── YAML register load ───────────────────────────────────────────────────────

def test_load_yaml_matches_bare_safe_load(tmp_path):
    """The 44 migrated sites all did `yaml.safe_load(open(path))`."""
    import yaml
    p = tmp_path / 'r.yaml'
    p.write_text('a: 1\nb: [x, y]\n', encoding='utf-8')
    with open(p, encoding='utf-8') as fh:
        expected = yaml.safe_load(fh)
    assert ci_common.load_yaml(p) == expected == {'a': 1, 'b': ['x', 'y']}


def test_load_yaml_RAISES_on_a_missing_file_unless_a_default_is_given(tmp_path):
    """THE CONTRACT THAT A FAILING TEST FORCED, and the most useful thing in this
    file.

    `load_yaml` first defaulted to `default=None`, so a migrated call site that had
    been a bare `open()` — which RAISES — began silently returning None on a
    missing input. That is the exact defect
    `test_engine_atlas.py::test_missing_input_is_reported_not_silently_absorbed`
    exists to prevent, and it CAUGHT the migration: 12 tests went red, five of them
    on this behaviour rather than on the stray `encoding=` kwarg.

    The fix is a sentinel, not a looser test. `load_yaml(p)` raises, exactly as the
    `open()` it replaced did, so every migration is delta-none; the forgiving mode
    is opt-in via an explicit default, which is what a caller reading an optional
    register (a lane file exists only once that lane has allocated an ED —
    CLAUDE.md §4) actually wants.
    """
    with pytest.raises(FileNotFoundError):
        ci_common.load_yaml(tmp_path / 'nope.yaml')
    assert ci_common.load_yaml(tmp_path / 'nope.yaml', {}) == {}
    assert ci_common.load_yaml(tmp_path / 'nope.yaml', None) is None
    (tmp_path / 'empty.yaml').write_text('', encoding='utf-8')
    assert ci_common.load_yaml(tmp_path / 'empty.yaml', {}) == {}
    assert ci_common.load_yaml(tmp_path / 'empty.yaml') is None


def test_load_yaml_is_delta_none_against_the_bare_open_it_replaced(tmp_path):
    """Expected-delta, both branches: present file and missing file."""
    import yaml
    p = tmp_path / 'r.yaml'
    p.write_text('a: 1\n', encoding='utf-8')
    with open(p, encoding='utf-8') as fh:
        assert ci_common.load_yaml(p) == yaml.safe_load(fh)
    missing = tmp_path / 'gone.yaml'
    old_exc = new_exc = None
    try:
        with open(missing, encoding='utf-8') as fh:
            yaml.safe_load(fh)
    except Exception as e:
        old_exc = type(e)
    try:
        ci_common.load_yaml(missing)
    except Exception as e:
        new_exc = type(e)
    assert old_exc is new_exc is FileNotFoundError


def test_load_yaml_does_not_swallow_a_syntax_error(tmp_path):
    """A malformed register must be loud. Returning the default here would turn
    a corrupt register into a silently-empty one — the exact shape of failure
    §1.6's dead-scope gates have."""
    import yaml
    (tmp_path / 'bad.yaml').write_text('a: [1, 2\n', encoding='utf-8')
    with pytest.raises(yaml.YAMLError):
        ci_common.load_yaml(tmp_path / 'bad.yaml', {})


def test_ci_common_does_not_import_yaml_at_module_level():
    """The layering claim in the module docstring, made falsifiable.

    Several BLOCKING gates are stdlib-only and import ci_common. If PyYAML
    became a module-level import here, every one of them would acquire a hard
    third-party dependency to read a constant.
    """
    src = (Path(ROOT) / 'tools' / 'ci_common.py').read_text(encoding='utf-8')
    module_level = [ln for ln in src.splitlines()
                    if re.match(r'^(import|from)\s+yaml\b', ln)]
    assert not module_level, f'yaml imported at module level: {module_level}'


# ── id_reservations: the plan row that had nothing behind it ─────────────────

def test_no_module_actually_loads_id_reservations():
    """The falsifier for a CORRECTION to the plan's §8.1 table.

    That table lists "id_reservations read | 8 | 1 | removed 7". Executing the
    step found zero parsers: the census's detector for the row is the bare string
    `id_reservations`, so its 8 are mentions — prose comments, one size-cap row
    keyed by path, one source tuple — not reads. There was nothing to collapse,
    and `ci_common` deliberately ships no reader for it.

    If a real loader ever appears, this test fails and that is the signal to give
    the primitive an owner — rather than the owner existing first with no caller,
    which is the build-then-disconnect defect ED-IN-0149 named.

    SELF-EXCLUSION IS NOT COSMETIC. Its first run failed on two files: this test
    (whose source contains `id_reservations` next to `safe_load` as the pattern it
    searches for) and `ci_common.py` (whose comment quotes the grep command). That
    is §2.4 verbatim — "a census that includes itself in its own population is a
    measurement defect, not a rounding error" — reproduced by the test written to
    guard the finding. Recorded here rather than silently fixed, because the audit
    documents the trap one section away from where I walked into it.
    """
    SELF_EXCLUDE = {
        'tests/valoria/test_ci_common_primitives.py',   # this file — the patterns it searches for
        'tools/ci_common.py',                           # quotes the grep command in a comment
    }
    loaders = []
    for dirpath, dirnames, filenames in os.walk(ci_common.REPO):
        dirnames[:] = [d for d in dirnames
                       if d not in {'.git', 'deprecated', '__pycache__', 'node_modules'}]
        for fn in filenames:
            if not fn.endswith('.py'):
                continue
            p = os.path.join(dirpath, fn)
            if os.path.relpath(p, ci_common.REPO).replace(os.sep, '/') in SELF_EXCLUDE:
                continue
            try:
                src = open(p, encoding='utf-8', errors='ignore').read()
            except OSError:
                continue
            for ln in src.splitlines():
                if 'id_reservations' in ln and re.search(r'safe_load|yaml\.load', ln):
                    loaders.append(f'{os.path.relpath(p, ci_common.REPO)}: {ln.strip()}')
    assert loaders == [], (
        'a real id_reservations loader now exists — give it an owner in ci_common '
        f'and update this test: {loaders}')


# ── the lazy re-export surface ───────────────────────────────────────────────

def test_lazy_reexports_resolve_to_obs_core():
    """§8.3's "single import surface" claim: the heavy primitives are reachable
    through ci_common and are the SAME objects, not copies."""
    sys.path.insert(0, os.path.join(ROOT, 'tools', 'observability'))
    import obs_core
    for name in ('read_ledger_entries', 'STATUS_RE', 'first_status', 'write_js_bundle'):
        assert getattr(ci_common, name) is getattr(obs_core, name), name


def test_lazy_reexport_is_actually_lazy():
    """Import ci_common in a fresh interpreter and assert obs_core did NOT come
    with it. Without this the __getattr__ is decorative — a plain
    `import obs_core` at the top would pass every other test in this file.
    """
    code = (
        'import sys; sys.path.insert(0, %r); import ci_common; '
        "print('obs_core' in sys.modules, 'yaml' in sys.modules)"
        % os.path.join(ROOT, 'tools')
    )
    out = subprocess.run([sys.executable, '-c', code], capture_output=True, text=True)
    assert out.returncode == 0, out.stderr
    assert out.stdout.strip() == 'False False', out.stdout


def test_unknown_attribute_still_raises():
    with pytest.raises(AttributeError):
        ci_common.no_such_primitive


# ── the recurrence guards (added 2026-08-12, ED-IN-0164) ─────────────────────
#
# ADDED IN RESPONSE TO AN ADVERSARIAL PASS, which made a charge that was correct
# and specific: G8 shipped a recurrence guard for `STATUS_RE`
# (test_status_reader_one_owner.test_only_one_status_regex_is_compiled_...) and G7
# shipped NONE for the five primitives it consolidated. CLAUDE.md §0.1 point 5 is
# unambiguous — "if you cannot write the guard you have not understood the
# pattern" — and the guard was demonstrably writable, because one of the six got
# it. Without these, tomorrow's sixteenth repo-root spelling fails nothing.
#
# The same pass also refuted the claim these guards now protect: "ZERO unmigrated
# repo-root definitions remain in tools/" was FALSE when published. Five live
# sites remained — build_incompleteness:43, build_proposals:32, build_glossary:66,
# session_open_work:39, trace_execution_phases:48 — four of them in modules whose
# siblings HAD been migrated, so it was a partial sweep reported as a complete one.
# They are migrated now, and this is what stops the claim rotting again.

def _tooling_py_files():
    out = []
    for base in ('tools', '.githooks'):
        for dirpath, dirnames, filenames in os.walk(os.path.join(ROOT, base)):
            dirnames[:] = [d for d in dirnames if d not in {'__pycache__', 'deprecated'}]
            for fn in filenames:
                if fn.endswith('.py'):
                    out.append(os.path.join(dirpath, fn))
    return out


# `tools/sim_harness/` is EXCLUDED, and the exclusion is a held ruling rather than
# convenience: the plan lists "the sim_harness promote-or-retire call (28 files)"
# among the items HELD FOR JORDAN. Migrating a cluster that may be retired whole is
# work done twice. It is named here so the exemption is visible, not silent.
_HELD_FOR_JORDAN = 'tools/sim_harness/'


def test_no_module_re_derives_the_repo_root():
    """The recurrence guard for §1.2's largest row: 53 sites, 15 spellings.

    A repo-root derivation is legitimate ONLY as the two-line bootstrap that
    imports the owner — a module cannot import ci_common without first knowing
    where ci_common is. That bootstrap anchors on the module's OWN directory, so
    the test is: does any module compute a path that walks ABOVE its own directory
    without then being the bootstrap?
    """
    strays = []
    for p in _tooling_py_files():
        rel = os.path.relpath(p, ROOT).replace(os.sep, '/')
        if rel.startswith(_HELD_FOR_JORDAN) or rel == 'tools/ci_common.py':
            continue
        src = open(p, encoding='utf-8', errors='ignore').read()
        for node in ast.walk(ast.parse(src)):
            if not isinstance(node, ast.Assign):
                continue
            expr = ast.unparse(node.value)
            if '__file__' not in expr:
                continue
            # walking above the module's own directory == deriving an ancestor
            ancestor = ('dirname(os.path.dirname' in expr
                        or re.search(r'parents\[\d+\]', expr)
                        or re.search(r"join\([^)]*'\.\.'", expr))
            if not ancestor:
                continue
            target = ast.unparse(node.targets[0])
            # the bootstrap itself is a sys.path.insert, never an assignment
            strays.append(f'{rel}:{node.lineno}: {target} = {expr}')
    assert not strays, (
        'a module derives an ancestor directory instead of using ci_common.REPO '
        f'(plan G7, ED-IN-0159 §8.1): {strays}')


def test_the_lane_roster_literal_appears_only_in_its_owner():
    """The recurrence guard for the roster. obs_core's header records that a prior
    copy silently OMITTED 'GO' — a whole lane undercounted — which is why a second
    copy is a defect and not merely repetition."""
    owners = []
    for p in _tooling_py_files():
        rel = os.path.relpath(p, ROOT).replace(os.sep, '/')
        if rel.startswith(_HELD_FOR_JORDAN):
            continue
        src = open(p, encoding='utf-8', errors='ignore').read()
        for i, ln in enumerate(src.splitlines(), 1):
            if ln.lstrip().startswith('#'):
                continue
            if re.search(r'''['"]MB['"]\s*,\s*['"]PC['"]\s*,\s*['"]FI['"]''', ln):
                owners.append(f'{rel}:{i}')
    assert owners == ['tools/ci_common.py:%d' % _lane_codes_line()], (
        f'the 9-lane roster literal exists outside its owner: {owners}')


def _lane_codes_line():
    src = (Path(ROOT) / 'tools' / 'ci_common.py').read_text(encoding='utf-8').splitlines()
    for i, ln in enumerate(src, 1):
        if ln.startswith('LANE_CODES'):
            return i
    raise AssertionError('ci_common.LANE_CODES definition not found')


def test_inline_token_estimation_is_confined_to_the_modules_being_retired():
    """`len(x) // 4` is the denominator every size cap in the repo is written in.

    Six inline sites survive and they are ALL in atomizer / doc_index_gen /
    index_gen, which plan step G2 retires — migrating a module scheduled for
    retirement is work done twice. This asserts the residue is exactly that set, so
    a NEW inline estimator anywhere else fails, and so this exemption cannot
    quietly outlive the retirement it is waiting on.
    """
    RETIRING = {'tools/atomizer.py', 'tools/doc_index_gen.py', 'tools/index_gen.py'}
    found = set()
    for p in _tooling_py_files():
        rel = os.path.relpath(p, ROOT).replace(os.sep, '/')
        if rel.startswith(_HELD_FOR_JORDAN) or rel == 'tools/ci_common.py':
            continue
        src = open(p, encoding='utf-8', errors='ignore').read()
        for ln in src.splitlines():
            if ln.lstrip().startswith('#'):
                continue
            if re.search(r'len\([^)]*\)\s*//\s*4', ln):
                found.add(rel)
    assert found <= RETIRING, f'a new inline token estimator appeared: {sorted(found - RETIRING)}'


def test_the_bare_yaml_load_residual_can_only_shrink():
    """`load_yaml` is the INTENDED owner, not the only loader, and its docstring
    says so. This pins the residual so the honest number cannot rot upward.

    52 bare `yaml.safe_load` calls remain in tools/, each doing something the
    helper does not — loading a stream, a string, or wanting the exception on a
    missing file. If this fails HIGH, a new bare call was added; if it fails LOW,
    migrate the count in the docstring with it.
    """
    total = 0
    for p in _tooling_py_files():
        rel = os.path.relpath(p, ROOT).replace(os.sep, '/')
        if rel == 'tools/ci_common.py':
            continue
        total += open(p, encoding='utf-8', errors='ignore').read().count('yaml.safe_load')
    assert total <= 52, f'bare yaml.safe_load count ROSE to {total} — a new copy was added'
    src = (Path(ROOT) / 'tools' / 'ci_common.py').read_text(encoding='utf-8')
    assert f'**{total} bare `yaml.safe_load` calls' in src or total == 52, (
        f'residual is now {total}; update load_yaml\'s docstring to match')


def test_every_ci_common_primitive_has_a_caller():
    """THE GUARD FOR THE DEFECT THIS FILE ITSELF SHIPPED.

    An adversarial pass found `ci_common` labelling id regexes, `load_yaml` and
    `load_register` "ONE OWNER" while NONE of them had a single caller outside this
    test file — the module refusing a speculative `read_id_reservations()` on one
    line for exactly that reason, and shipping three more fifty lines above. That
    is ED-IN-0149's build-then-disconnect defect, committed inside the commit that
    cites it.

    `load_register` was removed. The rest gained real call sites. This asserts the
    property directly, so the next speculative primitive fails here instead of
    surviving to the next census.
    """
    src_by_file = {}
    for p in _tooling_py_files():
        rel = os.path.relpath(p, ROOT).replace(os.sep, '/')
        if rel == 'tools/ci_common.py':
            continue
        src_by_file[rel] = open(p, encoding='utf-8', errors='ignore').read()

    PUBLIC = [n for n in vars(ci_common)
              if not n.startswith('_') and n not in {
                  'ast', 'glob', 'os', 're', 'subprocess', 'Path',
                  # documented lazy re-exports: reachable, but obs_core is their home
                  *ci_common._LAZY_FROM_OBS_CORE}]
    owner_src = (Path(ROOT) / 'tools' / 'ci_common.py').read_text(encoding='utf-8')
    owner_tree = ast.parse(owner_src)

    # INTERNAL USE, DETERMINED BY AST — not by string surgery.
    #
    # This clause was `owner_src.split(f'{name} =', 1)[-1]`, and it was VACUOUS for
    # every `def`-defined export: a function has no `name =` in the source, so
    # `split` returns a one-element list, `[-1]` yields the WHOLE FILE, and the
    # regex then matched the function's own `def` line. `load_yaml`, `doc_status`,
    # `tokens`, `read_text` and every `get_*` helper could have had zero callers
    # and passed.
    #
    # That is the exact defect this test exists to catch — `load_register` shipped
    # with no caller — so the guard was blind to its own incident class. THREE
    # INDEPENDENT ADVERSARIAL PASSES found it separately, which is §10's
    # rank-by-independent-rediscovery signal firing on a real defect rather than on
    # correlated blind spots.
    #
    # The replacement asks the parser: is this name LOADED anywhere in the owner
    # outside its own definition or assignment target? A `def` line is a
    # `FunctionDef`, never a `Name` load, so it cannot self-satisfy.
    internally_used = set()
    for node in ast.walk(owner_tree):
        if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
            internally_used.add(node.id)
        elif isinstance(node, ast.Attribute) and isinstance(node.ctx, ast.Load):
            internally_used.add(node.attr)

    uncalled = []
    for name in PUBLIC:
        # A primitive counts as called if a module names it through ci_common OR
        # through obs_core, which RE-EXPORTS the dependency-free ones under the
        # same names (dashboard_data reaches LEDGER_LANE_CODES that way), or if the
        # owner itself genuinely consumes it (EMPTY_TREE feeds _diff_args).
        via = (f'ci_common.{name}', f'obs_core.{name}', f'_obs_core.{name}')
        if any(v in s for s in src_by_file.values() for v in via):
            continue
        if name in internally_used:
            continue
        uncalled.append(name)
    assert not uncalled, (
        'ci_common exports primitives no module in tools/ uses — an abstraction '
        f'with no caller is the defect ED-IN-0149 named: {uncalled}')


def test_the_bootstrap_rationale_is_not_copy_pasted_across_the_tier():
    """G7's own comment was the duplication G7 exists to remove (ED-IN-0165).

    The migration attached a 5-line explanation of WHY the bootstrap is legitimate
    to every module it touched — 242 comment lines across 54 files, one
    explanation copy-pasted 54 times. That is precisely the defect class the step
    was executing against, committed by the execution: a rule with one owner, and
    its rationale with fifty-four.

    Found by measuring this branch's own line delta rather than by reading it:
    `tools/` grew +2,384/-896 lines while its NON-COMMENT delta was only
    +406/-226. The explanation now lives once, in `ci_common`'s module docstring,
    and each call site carries a three-line pointer to it.

    The assertion is on the LONG form, not on the pointer: pointers are supposed to
    repeat, explanations are not.
    """
    copies = []
    for p in _tooling_py_files():
        rel = os.path.relpath(p, ROOT).replace(os.sep, '/')
        if rel == 'tools/ci_common.py':
            continue
        src = open(p, encoding='utf-8', errors='ignore').read()
        if 'irreducible bootstrap' in src:
            copies.append(rel)
    assert not copies, (
        'the bootstrap rationale is being copy-pasted again — it belongs once, in '
        f"ci_common's docstring, with a pointer at each call site: {copies}")


def test_the_bootstrap_pointer_stays_short():
    """The pointer must not regrow into the explanation it replaced. Four lines is
    the budget: three of comment plus the `import ci_common` line."""
    import re as _re
    over = []
    for p in _tooling_py_files():
        rel = os.path.relpath(p, ROOT).replace(os.sep, '/')
        if rel == 'tools/ci_common.py':
            continue
        src = open(p, encoding='utf-8', errors='ignore').read()
        # Anchor on the pointer's OWN first line, not on "any run of comment lines
        # above the bootstrap". The greedy version flagged
        # tools/validate_ed_citations.py, whose pre-existing lane-roster comment
        # merely sits adjacent — a textual proxy capturing more than it means, the
        # same class of false positive this file has now produced three times
        # (the CLAUDE.md lane regex matching "IP world-tracks"; the `severity =`
        # regex matching a keyword argument). Measure the block that starts where
        # the pointer starts.
        m = _re.search(r'^(# Primitives \(repo root.*?)sys\.path\.insert\(0, os\.path[^\n]*\n'
                       r'import ci_common', src, _re.M | _re.S)
        if m and m.group(1).count('\n') > 4:
            over.append(f'{rel} ({m.group(1).count(chr(10))} comment lines)')
    assert not over, f'the bootstrap pointer is regrowing into an explanation: {over}'


def test_every_lane_display_map_is_total_over_the_owner():
    """The roster guard the tuple-spelling one could not see (ED-IN-0165).

    `test_the_lane_roster_literal_appears_only_in_its_owner` matches
    `'MB','PC','FI'` adjacent on one line — the TUPLE spelling. Two live DICT
    enumerations evaded it entirely (`build_decisions.LANE_NAMES`,
    `dashboard_data.LANE_NAMES`), and they had already diverged: 'SE' read
    "Settlements" in one and "settlement / territory" in the other; 'FA'
    "Faction actions" vs "faction / political".

    That is CLAUDE.md §8's same-name-divergent-value class, live in the tree, while
    G7 reported the roster collapsing "9 -> 3". The figure was wrong on CONCEPT:
    the census pattern-matched a spelling, not the roster, and the guard inherited
    the blind spot — the exact error §2.1 of the findings document names as the
    costliest in this project, committed by the step that quotes it.

    Display strings stay per-surface on purpose (the dashboard's lower-case card
    vocabulary is not the ledger's title-case one). What must not diverge is WHICH
    LANES EXIST, so this asserts each map is TOTAL over the owner.
    """
    sys.path.insert(0, os.path.join(ROOT, 'tools', 'observability'))
    import build_decisions
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        'dashboard_data', os.path.join(ROOT, 'tools', 'dashboard_data.py'))
    dd = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(dd)

    for label, mapping in (('build_decisions.LANE_NAMES', build_decisions.LANE_NAMES),
                           ('dashboard_data.LANE_NAMES', dd.LANE_NAMES)):
        assert set(mapping) == set(ci_common.LANE_CODES), (
            f'{label} is not total over the owner: '
            f'missing {set(ci_common.LANE_CODES) - set(mapping)}, '
            f'extra {set(mapping) - set(ci_common.LANE_CODES)}')
        assert all(v for v in mapping.values()), f'{label} has an empty display name'
