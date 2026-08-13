"""
Unit tests for `tools/evacuation_plan.py` — the keep/relocate/evacuate partition (ED-IN-0128).

WHY A DELETION PLANNER NEEDS A TEST MORE THAN MOST TOOLS. Its output authorises removing most of
the tree — a four-figure number that MOVES with every rule change, which is why this docstring no
longer states it: it said "1,996" while the tool's own manifest said 1,467, having gone stale
across the rule changes it was describing. Run `python3 tools/evacuation_plan.py` for the current
count. Every other tool in `tools/` fails visibly when it is wrong; this one fails by quietly
assigning a file to the wrong side, and the failure is only observable after the deletion.

THE DEFECT CLASS IT GUARDS. `build_fork.py`'s `CARRY`/`LEAVE` read like a partition and are not
one — `CARRY ∪ LEAVE` leaves a large neither-set (`.github/`, `tools/`, `tests/valoria/`,
`CLAUDE.md`, …). Under extraction that set silently defaults to left-behind, which is harmless;
under evacuation the mirror operation deletes it, taking the enforcement tier and the shipping
gate. **The bug was in neither list — it was in assuming two lists cover the tree.** So the
headline test here is totality, and `test_the_totality_guard_can_fail` is the positive control
that stops totality from being vacuously true.

`test_ordering_is_load_bearing` exists because the rules are FIRST-MATCH-WINS. A file can match
several; only the order decides. Order-dependence that nothing pins is a latent reordering bug.
"""
import os
import sys

import pytest

HERE = os.path.dirname(__file__)
TOOLS = os.path.join(HERE, '..', '..', 'tools')
sys.path.insert(0, TOOLS)
import evacuation_plan as ep  # noqa: E402


@pytest.fixture(scope='module')
def part():
    return ep.partition()


# --------------------------------------------------------------------------------------
# Totality — the headline property
# --------------------------------------------------------------------------------------

def test_partition_is_total(part):
    """Every tracked file gets a verdict. No neither-set."""
    orphans = part['buckets']['UNPARTITIONED']
    assert orphans == [], (
        f"{len(orphans)} tracked file(s) match no rule, e.g. {orphans[:5]}. "
        "A file with no verdict is exactly the CARRY-union-LEAVE defect: under a mirror-image "
        "deletion it would be removed without ever appearing in a plan.")


def test_partition_covers_every_tracked_file(part):
    """The buckets sum to the tree — no file counted twice, none dropped."""
    b = part['buckets']
    total = sum(len(v) for v in b.values())
    assert total == len(ep.tracked())
    everything = [p for v in b.values() for p in v]
    assert len(set(everything)) == total, "a file appears in more than one bucket"


def test_the_totality_guard_can_fail():
    """POSITIVE CONTROL (CLAUDE.md §0.1 point 2).

    If `classify` returned a verdict for everything unconditionally, `test_partition_is_total`
    would pass while guaranteeing nothing. A path under no rule must come back UNPARTITIONED.
    """
    verdict, rule_id, _ = ep.classify('some_unrooted_dir/thing.txt')
    assert verdict == 'UNPARTITIONED'
    assert rule_id == 'R-NONE'


# --------------------------------------------------------------------------------------
# The verdicts that would hurt most if they flipped
# --------------------------------------------------------------------------------------

@pytest.mark.parametrize('rel,expected', [
    # the enforcement tier and session protocol — the CARRY/LEAVE casualties
    ('tools/valoria_local.py', 'keep'),
    ('tests/valoria/test_key_graph.py', 'keep'),
    ('.github/workflows/valoria-ci.yml', 'keep'),
    ('.githooks/pre-commit', 'keep'),
    ('CLAUDE.md', 'keep'),
    ('CURRENT.md', 'keep'),
    # code
    ('engine/mc_v18.py', 'keep'),
    ('engine/substrate/keys.py', 'keep'),
    ('systems/mass_battle/sim/massbattle.py', 'keep'),
    # prose with NO code pair -> authoritative spec
    ('canon/philosophical_foundations.md', 'keep'),
    # prose WITH a code pair, WHERE THE CODE SUPERSEDED IT -> the prose goes (Jordan, 2026-08-04),
    # gated on tools/export_params_constants.py having captured the tables verbatim first.
    # This row read 'keep' until ED-IN-0139; it is flipped deliberately, not by rule drift.
    ('engine/params/core.md', 'evacuate'),
    # …but the CAPTURE it evacuates into is code-adjacent data and stays
    ('engine/engine_params/params_tables.yaml', 'keep'),
    # canon engine misfiled under an evacuating parent
    ('tests/sim/mass_battle/orchestration.py', 'keep'),
    # detritus
    ('deprecated/tools/propagator.py', 'evacuate'),
    ('arcs/simulated/arcs_01_04.md', 'evacuate'),
])
def test_known_files_land_correctly(rel, expected):
    """Pins the verdicts whose flip would be most expensive. Paths need not all exist."""
    verdict, _, _ = ep.classify(rel)
    assert verdict == expected, f'{rel} classified {verdict}, expected {expected}'


def test_ordering_is_load_bearing():
    """FIRST-MATCH-WINS: these files match a later, opposite rule too.

    `tests/sim/mass_battle/x.py` matches R-MB-CANON (keep) and R-TESTS-PROSE (evacuate).
    A reordering that put the general rule first would evacuate the canon engine, and totality
    would still pass. This is the test that notices.
    """
    assert ep.classify('tests/sim/mass_battle/engine.py')[1] == 'R-MB-CANON'
    assert ep.classify('tests/sim/other_stress/notes.md')[1] == 'R-TESTS-PROSE'
    # generated output beats the two-week keep, at any date
    assert ep.classify('audit/2026-07-29-scenario-visualization/contact_sheet.png')[0] == 'evacuate'


# --------------------------------------------------------------------------------------
# The audit date rule
# --------------------------------------------------------------------------------------

def test_undated_audit_entries_are_not_recent():
    """`audit/lane-a/…` and bare files carry no date; they must not sneak through the window."""
    assert ep._audit_is_recent('audit/lane-a/whatever.md') is False
    assert ep._audit_is_recent('audit/valoria_how_to_play.md') is False
    assert ep.classify('audit/lane-a/whatever.md')[0] == 'evacuate'


def test_audit_cutoff_boundary():
    """On the cutoff date is IN; the day before is OUT.

    Derived from AUDIT_CUTOFF rather than hardcoded, so moving the cutoff (two weeks -> all of
    July, 2026-08-04) re-aims the test instead of silently falsifying it.
    """
    import datetime as _dt
    cutoff = _dt.date.fromisoformat(ep.AUDIT_CUTOFF)
    day_before = (cutoff - _dt.timedelta(days=1)).isoformat()
    assert ep._audit_is_recent(f'audit/{ep.AUDIT_CUTOFF}-x/f.md') is True
    assert ep._audit_is_recent(f'audit/{day_before}-x/f.md') is False
    # a date unambiguously before any plausible cutoff
    assert ep._audit_is_recent('audit/2026-04-30-x/f.md') is False


def test_generated_output_evacuates_but_its_generator_does_not():
    """The 36 MB render directory is six days old: age alone would keep it."""
    d = 'audit/2026-07-29-scenario-visualization/'
    assert ep.classify(d + 'contact_sheet_historical.png')[0] == 'evacuate'
    assert ep.classify(d + 'scenarios_historical.html')[0] == 'evacuate'
    assert ep.classify(d + 'render_scenarios.py')[0] == 'relocate'


# --------------------------------------------------------------------------------------
# Relocation and the contract guard
# --------------------------------------------------------------------------------------

def test_relocations_land_in_a_subsystem(part):
    """Jordan: "visualization tool for mb should be moved to mb and wiring should be to systems"."""
    moves = part['moves']
    assert moves, 'expected at least the MB visualisation instruments to relocate'
    OK = ('systems/', 'engine/', 'registers/')
    for src, dest in moves.items():
        assert dest.startswith(OK), f'{src} relocates to no proper home: {dest}'
        # the whole point is leaving the evacuating trees
        assert not dest.startswith(('audit/', 'deprecated/', 'research/'))


def test_no_contracted_unit_is_evacuated(part):
    """A unit with a contract but no code YET is the backlog, not dead weight."""
    bad = ep.contract_guard(set(part['buckets']['evacuate']))
    assert bad == [], f'contracted/stub units inside the evacuate set: {bad}'


def test_contract_guard_can_fail():
    """POSITIVE CONTROL: plant a contracted path in the evacuate set and require a complaint."""
    planted = ep.contract_guard({'systems/mass_battle/mass_battle_v30.md'})
    assert planted, 'the contract guard did not object to evacuating a contracted doc'


# --------------------------------------------------------------------------------------
# Split-path readers — the false negative that a substring scan cannot fix
# --------------------------------------------------------------------------------------

def test_split_path_scan_finds_what_substring_scan_cannot():
    """The concrete miss: gen_sigma_parity_goldens.py built its oracle path from segments.

        os.path.join(REPO_ROOT, 'audit', '2026-06-03-contest-groundup', 'engine.py')

    contains no literal 'audit/', so `readers()` reported that file as unread while a kept tool
    loaded it to regenerate a committed golden a kept CI test asserts on.

    PLANTED, NOT LIVE (2026-08-05): the evacuate set is now EMPTY — the terminal state — so a test
    reading the live partition would assert the job is unfinished. The property under test is the
    SCAN, and the scan is exercised directly.
    """
    import tempfile, textwrap, os as _os
    with tempfile.TemporaryDirectory(dir=_os.path.join(HERE, '..', '..')) as d:
        rel = _os.path.relpath(d, _os.path.join(HERE, '..', '..'))
        with open(_os.path.join(d, 'probe.py'), 'w', encoding='utf-8') as fh:
            fh.write(textwrap.dedent("""
                import os
                P = os.path.join(REPO, 'audit', '2026-06-03-contest-groundup', 'engine.py')
            """))
        planted = {'audit/2026-06-03-contest-groundup/engine.py'}
        hits = ep.joined_path_readers(['audit'], [_os.path.join(rel, 'probe.py')], planted)
        assert hits['audit'], 'a constructed path into an evacuating tree was not detected'


def test_the_split_scan_can_fail():
    """POSITIVE CONTROL: the scan must NOT report a constructed path that is not evacuating.

    Previously this planted a path into `deprecated/` and required a hit. `deprecated/` no longer
    evacuates wholesale, so the control now checks the other direction — the one that actually
    protects a deletion plan from crying wolf.
    """
    import tempfile, textwrap, os as _os
    with tempfile.TemporaryDirectory(dir=_os.path.join(HERE, '..', '..')) as d:
        rel = _os.path.relpath(d, _os.path.join(HERE, '..', '..'))
        with open(_os.path.join(d, 'probe.py'), 'w', encoding='utf-8') as fh:
            fh.write(textwrap.dedent("""
                import os
                P = os.path.join(REPO, 'engine', 'substrate', 'keys.py')
            """))
        # the retained list must contain the kept file, or 'engine' itself reads as wholly
        # evacuating and the scan is right to flag it — the same mixed-prefix subtlety the
        # production fix was about.
        hits = ep.joined_path_readers(['engine'],
                                      [_os.path.join(rel, 'probe.py'), 'engine/substrate/keys.py'],
                                      {'engine/params/core.md'})
        assert not hits['engine'], \
            'a path into a KEPT subtree was reported as a split-path breakage'


def test_a_partly_evacuating_root_slices_to_its_evacuating_subtree():
    """A slice must never name a prefix containing a KEPT file.

    `engine/` was the first root that only PARTLY evacuated, and it broke the reader scan: the
    pattern `engine/` matched nearly every kept file. PLANTED now that the evacuate set is empty —
    the invariant is about `slice_prefixes`, not about the live partition.
    """
    evac = ['a/gone/x.md', 'a/gone/y.md', 'b/mixed/gone.md']
    retained = ['a/kept_sibling.md', 'b/mixed/kept.md', 'b/other.md']
    prefixes = ep.slice_prefixes(evac, retained)
    assert prefixes['a'] == ['a/gone'], f"expected the slice to be a/gone, got {prefixes['a']}"
    assert prefixes['b'] == ['b/mixed/gone.md'], \
        f"a prefix containing a kept file must not be a slice, got {prefixes['b']}"
    for prefs in prefixes.values():
        for pre in prefs:
            assert not [r for r in retained if r == pre or r.startswith(pre + '/')], \
                f'slice {pre} contains a kept file'


def test_split_path_hits_require_a_WHOLLY_evacuating_target(part):
    """`tests/sim` held both evacuating stress prose and the KEPT canon mass-battle engine.

    Testing "something under this path evacuates" reported all 30 kept readers of the canon engine
    as split-path breakages. Wholly-evacuating is the property that predicts an actual break.

    THE EVACUATE SET WAS EMPTIED (2026-08-05, ED-IN-0145) — the terminal state this whole tool was
    built to reach.

    ⚠ IT IS NOT EMPTY ANY MORE, and this docstring said otherwise until 2026-08-13 (ED-IN-0177).
    The G2 retirement moved three tools INTO `deprecated/tools/` under Jordan's ruling
    (ED-IN-0171), and `R-DEPRECATED` classifies everything under `deprecated/` as 'evacuate' —
    so the set repopulated the moment the ruling was executed. "Terminal state" was true for
    eight days and then quietly stopped being true; nothing failed, because this test was
    already written to hold either way.

    That is the point worth keeping: the assertion below is unaffected because it checks the
    PREDICATE against planted inputs rather than the live partition — it must call a mixed
    prefix non-evacuating and a wholly-evacuating one evacuating, whatever the live partition
    happens to be. A version of this test that had asserted "the set is empty" would now be
    red for a correct change. The prose was the only thing that rotted, which is why it is
    corrected rather than deleted.
    """
    evac = set(part['buckets']['evacuate'])
    retained = part['buckets']['keep'] + part['buckets']['relocate']
    if not evac:
        # Planted, not live: the predicate must still discriminate.
        planted = {'x/gone/a.md', 'x/gone/b.md', 'y/mixed/gone.md'}
        pure = ep.pure_prefixes(sorted(planted), retained + ['y/mixed/kept.md'])
        assert ep._is_evacuating_path('x/gone', pure, planted) is True
        assert ep._is_evacuating_path('y/mixed', pure, planted) is False, \
            'a prefix containing a KEPT file must not count as evacuating'
        return
    pure = ep.pure_prefixes(sorted(evac), retained)
    jr = ep.joined_path_readers(sorted({e.split('/')[0] for e in evac}), retained, evac)
    flat = [h for lst in jr.values() for h in lst]
    assert not any('test_mass_battle_byte_exact' in h for h in flat), \
        'a kept reader of the kept canon MB engine is being reported as a split-path breakage'

def test_the_parity_oracle_is_not_evacuated():
    """Regression pin for the casualty that motivated the split-path scan.

    tools/gen_sigma_parity_goldens.py regenerates engine/tests/goldens/sigma_leverage_parity.json;
    engine/tests/test_sigma_leverage_parity.py asserts on it. Evacuating the oracle leaves a
    committed generated table with no source.
    """
    verdict, rule_id, _ = ep.classify('audit/2026-06-03-contest-groundup/engine.py')
    assert verdict == 'relocate', f'the ground-up parity oracle must survive, got {verdict}'
    dest, _, _ = ep.relocation('audit/2026-06-03-contest-groundup/engine.py')
    assert dest.startswith('engine/reference/'), (
        f'the oracle belongs with the code it validates, not in audit/: {dest}')


def test_the_ed_universe_survives_evacuation(part):
    """The blocking citation gate reads its ED universe from three deprecated/ dirs.

    Evacuating them turns `validate_ed_citations` red on the evacuation commit — its own docstring
    records losing ONE such dir turning 110 valid citations into NONEXISTENT. They must survive.
    """
    evac = set(part['buckets']['evacuate'])
    import fnmatch
    stranded = [p for p in evac
                if p.startswith(('deprecated/archives/editorial/',
                                 'deprecated/archives/editorials/', 'deprecated/canon/'))
                and ('ledger' in os.path.basename(p) or 'editorial' in os.path.basename(p))]
    assert stranded == [], (
        f'{len(stranded)} ED-archive file(s) in the evacuate set would break the blocking '
        f'citation gate, e.g. {stranded[:3]}')


# --------------------------------------------------------------------------------------
# Doc↔tool agreement — the falsifier for prose that restates a machine value
# --------------------------------------------------------------------------------------

def test_keep_set_doc_cutoff_matches_the_tool():
    """The keep-set doc must not restate a cutoff the tool disagrees with.

    WHY THIS TEST EXISTS. `repository_keep_set_v1.md` stated `2026-07-21` for a full day after
    Jordan widened the window to `2026-07-01` — the doc and the tool disagreed about the rule that
    decides ~500 files. That is the two-surfaces-drift failure this whole programme keeps hitting:
    `CARRY`/`LEAVE` vs the tree, a proposal vs the manifest, this doc vs `evacuation_plan`. A prose
    correction with no guard just resets the clock until the next ruling.

    So: any ISO date the doc presents as THE audit cutoff must equal `AUDIT_CUTOFF`. The doc is free
    to mention other dates (ledger entries, incident dates); only the ones marked as the cutoff bind.
    """
    doc = os.path.join(HERE, '..', '..', 'systems', '_architecture', 'repository_keep_set_v1.md')
    with open(doc, encoding='utf-8') as fh:
        text = fh.read()

    # Lines that state the audit cutoff: an `audit/` row carrying a >= or < comparison.
    import re
    stated = set()
    for line in text.splitlines():
        if '`audit/`' in line and ('≥' in line or '<' in line):
            stated.update(re.findall(r'\d{4}-\d{2}-\d{2}', line))

    assert stated, (
        'no audit-cutoff row found in the keep-set doc — either the doc stopped stating the rule '
        '(fine, delete this test) or the row format changed and this guard has gone blind')
    assert stated == {ep.AUDIT_CUTOFF}, (
        f'keep-set doc states audit cutoff(s) {sorted(stated)} but the tool uses '
        f'{ep.AUDIT_CUTOFF!r}. The doc and the partition-of-record disagree about the rule that '
        f'decides the largest slice.')
