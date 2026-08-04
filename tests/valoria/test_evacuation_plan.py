"""
Unit tests for `tools/evacuation_plan.py` — the keep/relocate/evacuate partition (ED-IN-0128).

WHY A DELETION PLANNER NEEDS A TEST MORE THAN MOST TOOLS. Its output authorises removing 1,996
files. Every other tool in `tools/` fails visibly when it is wrong; this one fails by quietly
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
    # prose WITH a code pair -> information only, still kept
    ('engine/params/core.md', 'keep'),
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
    for src, dest in moves.items():
        assert dest.startswith('systems/'), f'{src} relocates outside systems/: {dest}'
        assert not dest.startswith('audit/')


def test_no_contracted_unit_is_evacuated(part):
    """A unit with a contract but no code YET is the backlog, not dead weight."""
    bad = ep.contract_guard(set(part['buckets']['evacuate']))
    assert bad == [], f'contracted/stub units inside the evacuate set: {bad}'


def test_contract_guard_can_fail():
    """POSITIVE CONTROL: plant a contracted path in the evacuate set and require a complaint."""
    planted = ep.contract_guard({'systems/mass_battle/mass_battle_v30.md'})
    assert planted, 'the contract guard did not object to evacuating a contracted doc'
