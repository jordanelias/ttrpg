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

def test_split_path_scan_finds_what_substring_scan_cannot(part):
    """The concrete miss: gen_sigma_parity_goldens.py builds its oracle path from segments.

        os.path.join(REPO_ROOT, 'audit', '2026-06-03-contest-groundup', 'engine.py')

    contains no literal 'audit/', so `readers()` reported that file as unread while a kept tool
    loaded it to regenerate a committed golden a kept CI test asserts on. This pins the AST scan
    that catches it, and `test_the_split_scan_can_fail` below stops it passing vacuously.
    """
    retained = part['buckets']['keep'] + part['buckets']['relocate']
    roots = sorted({e.split('/')[0] for e in part['buckets']['evacuate']})
    jr = ep.joined_path_readers(roots, retained)
    flat = [h for lst in jr.values() for h in lst]
    assert flat, 'the split-path scan found nothing at all — it has stopped working'
    # deprecated/ is evacuating and has kept-code readers built from segments
    assert any('currency_consistency_check.py' in h for h in flat), \
        'currency_consistency_check.py builds a deprecated/skills path from segments; not detected'


def test_the_split_scan_can_fail():
    """POSITIVE CONTROL: a constructed path into an evacuating root must be reported.

    Without this, a scanner that returned [] for everything would satisfy the test above only by
    accident of another hit existing.
    """
    import tempfile, textwrap
    with tempfile.TemporaryDirectory(dir=os.path.join(HERE, '..', '..')) as d:
        rel = os.path.relpath(d, os.path.join(HERE, '..', '..'))
        f = os.path.join(d, 'probe.py')
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(textwrap.dedent("""
                import os
                P = os.path.join(REPO, 'deprecated', 'tools')
            """))
        hits = ep.joined_path_readers(['deprecated'], [os.path.join(rel, 'probe.py')])
        assert hits['deprecated'], 'planted split path into deprecated/ was not detected'


def test_a_partly_evacuating_root_slices_to_its_evacuating_subtree(part):
    """`engine/` is the first root that is only PARTLY evacuating, and it broke the reader scan.

    The scan used to search kept files for the evacuating file's TOP-LEVEL directory. With
    `engine/params/` flipped to evacuate (ED-IN-0139), the pattern `engine/` matches nearly every
    kept file in the tree, so a 43-file slice would report hundreds of blocking readers that have
    nothing to do with it. `slice_prefixes` must therefore hand back `engine/params`, never
    `engine`.
    """
    prefixes = ep.slice_prefixes(part['buckets']['evacuate'],
                                 part['buckets']['keep'] + part['buckets']['relocate'])
    assert prefixes['engine'] == ['engine/params'], (
        f"expected the engine slice to be exactly engine/params, got {prefixes['engine']}. "
        "A slice that names a root containing kept code cannot produce a usable reader count.")
    # and no slice may name a prefix that contains something we are keeping
    retained = set(part['buckets']['keep'] + part['buckets']['relocate'])
    for root, prefs in prefixes.items():
        for p in prefs:
            clashes = [r for r in retained if r == p or r.startswith(p + '/')]
            assert not clashes, f'slice {p} contains kept file(s), e.g. {clashes[:2]}'


def test_split_path_hits_require_a_WHOLLY_evacuating_target(part):
    """`tests/sim` holds both evacuating stress prose and the KEPT canon mass-battle engine.

    Testing "something under this path evacuates" reported all 30 kept readers of the canon engine
    as split-path breakages — 30 false alarms on the single most load-bearing kept tree under an
    evacuating root. Wholly-evacuating is the property that predicts an actual break.
    """
    evac = set(part['buckets']['evacuate'])
    retained = part['buckets']['keep'] + part['buckets']['relocate']
    pure = ep.pure_prefixes(sorted(evac), retained)
    assert ep._is_evacuating_path('tests/sim', pure, evac) is False, \
        'tests/sim contains the kept canon mass-battle engine and must not count as evacuating'
    assert ep._is_evacuating_path('engine/params', pure, evac) is True
    # `deprecated/skills` was wholly evacuating until the W3 rehearsal (ED-IN-0144) proved a
    # BLOCKING CI gate transitively imports two files inside it (compliance_check -> github_ops
    # -> index_bootstrap ...). It is now MIXED, and this assertion says so rather than being
    # weakened: the property under test is that a mixed prefix does NOT count as evacuating.
    assert ep._is_evacuating_path('deprecated/skills', pure, evac) is False, \
        'deprecated/skills holds kept, import-load-bearing files — it is not wholly evacuating'
    # anti-vacuity: a prefix that IS wholly evacuating must still be detected. Note how few
    # qualify now -- deprecated/archives does not either, because the ED-universe files relocate
    # out of it. Nearly every evacuating root has a kept island in it, which is the whole reason
    # the slice unit is a computed pure prefix and not a directory name.
    assert ep._is_evacuating_path('arcs', pure, evac) is True, \
        'a genuinely wholly-evacuating prefix must still be detected'
    # the concrete false alarm this removed
    jr = ep.joined_path_readers(sorted({e.split('/')[0] for e in evac}), retained, evac)
    flat = [h for lst in jr.values() for h in lst]
    assert not any('test_mass_battle_byte_exact' in h for h in flat), \
        'a kept reader of the kept canon MB engine is being reported as a split-path breakage'
    assert flat, 'the split-path scan found nothing at all — the tightening went too far'


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
