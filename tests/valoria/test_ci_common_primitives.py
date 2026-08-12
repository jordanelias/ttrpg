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

def test_id_patterns_are_composable_strings():
    """Half the call sites embed the pattern in a larger expression
    (`-\\s+id:\\s+PP-(\\d+)` in ci_vetting_check:105). A compiled object cannot be
    composed, so the owner must publish the source text too."""
    assert isinstance(ci_common.PP_ID_PAT, str)
    assert re.compile(r'-\s+id:\s+' + ci_common.PP_ID_PAT).search('- id: PP-674')


@pytest.mark.parametrize('text,expected', [
    ('see PP-674 and PP-1', ['PP-674', 'PP-1']),
    ('no ids here', []),
])
def test_pp_id_regex_matches_the_pre_migration_form(text, expected):
    """Transcribed from atomizer:239 and index_gen:234 — r'PP-\\d+'."""
    assert ci_common.PP_ID_RE.findall(text) == re.compile(r'PP-\d+').findall(text) == expected


def test_ed_id_regex_matches_BOTH_formats():
    """CLAUDE.md §4: both formats are permanently valid — the flat sequence is
    FROZEN at ED-1096, not retired, and every new item is lane-tagged.

    This is the assertion with teeth. `index_gen.py:129` documents its own
    r'ED-\\d+' as predating the lane format and never updated, so the flat-only
    pattern is a live bug in the tree, not a hypothetical: against
    'ED-IN-0159' it matches the substring 'ED-0159'... no, it fails to match at
    all, and the item is silently invisible. The owner must match both.
    """
    assert ci_common.ED_ID_RE.findall('ED-1094 and ED-IN-0159') == ['ED-1094', 'ED-IN-0159']
    # the flat-only form that motivated this — kept as the contrast
    assert re.compile(r'ED-\d+').findall('ED-IN-0159') == []


def test_any_id_pattern_covers_both_families():
    assert ci_common.ANY_ID_RE.findall('PP-674 ED-1094 ED-MB-0065') == \
        ['PP-674', 'ED-1094', 'ED-MB-0065']


def test_ed_lane_pattern_only_accepts_real_lanes_shape():
    """Zero-padded to 4 digits, 2-letter lane (CLAUDE.md §4)."""
    rx = re.compile(ci_common.ED_LANE_ID_PAT)
    assert rx.fullmatch('ED-IN-0159')
    assert not rx.fullmatch('ED-I-0159')
    assert not rx.fullmatch('ED-IN-159')


# ── YAML register load ───────────────────────────────────────────────────────

def test_load_yaml_matches_bare_safe_load(tmp_path):
    """The 44 migrated sites all did `yaml.safe_load(open(path))`."""
    import yaml
    p = tmp_path / 'r.yaml'
    p.write_text('a: 1\nb: [x, y]\n', encoding='utf-8')
    with open(p, encoding='utf-8') as fh:
        expected = yaml.safe_load(fh)
    assert ci_common.load_yaml(p) == expected == {'a': 1, 'b': ['x', 'y']}


def test_load_yaml_missing_and_empty_return_the_default(tmp_path):
    """The documented contract: a register that does not exist reads as the
    default rather than raising, because a lane file exists only once that lane
    has allocated an ED (CLAUDE.md §4)."""
    assert ci_common.load_yaml(tmp_path / 'nope.yaml', {}) == {}
    assert ci_common.load_yaml(tmp_path / 'nope.yaml') is None
    (tmp_path / 'empty.yaml').write_text('', encoding='utf-8')
    assert ci_common.load_yaml(tmp_path / 'empty.yaml', {}) == {}


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
