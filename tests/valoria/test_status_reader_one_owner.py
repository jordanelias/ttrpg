"""The EXPECTED-DELTA test for plan step G8 (ED-IN-0159 §1.3a).

G8 is the ONE intended behaviour change in Track G, and the plan is specific about
what its test owes:

    "Its test must name all 7 disputed docs AND ASSERT BOTH DIRECTIONS (§1.3a)"
    "A one-sided test lets the incompleteness census silently shrink"

So every assertion below is paired: what each migrated reader GAINS and what it
LOSES. A test that only checked gains would pass while `build_incompleteness`
quietly stopped seeing documents, which is the specific failure the plan names.

────────────────────────────────────────────────────────────────────────────────
THREE CORRECTIONS TO §1.3a, each measured here rather than asserted
────────────────────────────────────────────────────────────────────────────────

1. THERE ARE FOUR LIVE READERS, NOT FIVE. §1.3a's table lists
   `dashboard_data._STATUS_RE = ^#{1,3}\\s*Status:`. That attribute does not exist:
   `dashboard_data.py:695` calls `obs_core.first_status`, and it has done so since
   obs_core was built. The census transcribed the pattern from obs_core's own
   HISTORICAL COMMENT recording the regex it replaced — a comment describing a
   past state, read as a present one. Every "invisible to: dashboard_data" cell in
   the disputed table is therefore wrong: dashboard_data sees exactly what the
   canonical owner sees. `test_dashboard_data_has_no_independent_status_regex`
   pins the correction.

2. THE DELTA IS ONE-SIDED, NOT TWO-SIDED. §1.3a predicted that collapsing onto the
   owner "*adds* documents to two parsers' view and can *remove* them from a
   third's". Measured: `ci_generation_consistency` gains and loses nothing (its
   regex was already equivalent — 206 docs, identical set), `build_incompleteness`
   gains and loses nothing in its own scope (25 -> 25), and only
   `build_identifier_census` moves. The prediction was reasonable and wrong; the
   test asserts the measurement.

3. THE DIVERGENCE THAT MATTERED WAS THE WINDOW, NOT THE REGEX. Three of the four
   readers scan different amounts of each file (12 lines / 80 / whole document),
   and §1.3a compared their regexes by running all five over WHOLE documents —
   which is how none of them is used. Over a whole document the canonical pattern
   matches a schema template and a legend. `ci_common.STATUS_HEAD_LINES` makes the
   window a named constant, chosen by the measurement in
   `test_window_choice_is_the_one_that_flips_no_superseded_classification`.
"""
import os
import re
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'observability'))

import ci_common  # noqa: E402

# The seven documents §1.3a named as DISPUTED, verbatim and in its order.
DISPUTED = [
    'workplans/valoria_master_workplan_v6.md',
    'systems/ui/valoria_ui_ux_v4.md',
    'references/restructure_ledger.md',
    'engine/sim_reference_CONVENTIONS.md',
    'systems/combat/combat_engine_v1/README.md',
    'skills/valoria-simulator/SKILL.md',
    'audit/2026-08-06-social-contest-three-lens-audit/sources/03_consolidation.md',
]

# The pre-migration regexes, transcribed from the sources they were removed from.
OLD_BIC = re.compile(r'^##\s*Status:\s*(.+)$', re.M)                 # build_identifier_census:282
OLD_CGC = re.compile(r'\s*#{0,3}\s*Status\s*:\s*(.+)', re.I)         # ci_generation_consistency:60
OLD_BIN = re.compile(                                                # build_incompleteness:315
    r'^\s*#{0,4}\s*Status\s*:\s*.*?\b'
    r'(PROPOSED|PROVISIONAL|DRAFT|STALE|SUPERSEDED|DEPRECATED|WIP|TODO)\b', re.I | re.M)


def tracked_md():
    out = subprocess.run(['git', 'ls-files', '*.md'], cwd=ROOT,
                         capture_output=True, text=True).stdout.split()
    return [p for p in out if not p.startswith('deprecated/')]


def read(rel):
    try:
        return (Path(ROOT) / rel).read_text(encoding='utf-8', errors='ignore')
    except OSError:
        return ''


# ── the disputed seven, individually accounted for ───────────────────────────

def test_every_disputed_doc_still_exists():
    """If one is renamed or removed, the accounting below silently stops meaning
    anything. Fail loudly instead."""
    missing = [d for d in DISPUTED if not (Path(ROOT) / d).is_file()]
    assert missing == [], f'disputed docs no longer in the tree: {missing}'


def test_the_disputed_seven_are_exactly_build_identifier_census_blind_spot():
    """The whole of §1.3a's disputed set, explained by ONE cause.

    Over whole documents, the set the canonical owner sees minus the set the old
    `^##\\s*Status:` saw is exactly these seven — because that regex required
    EXACTLY TWO HASHES, and the seven use one hash, no hash, bold, or indentation.
    Not "five regexes disagree": one regex was narrow.
    """
    canon, old = set(), set()
    for d in tracked_md():
        t = read(d)
        if ci_common.first_status(t) is not None:
            canon.add(d)
        if OLD_BIC.search(t):
            old.add(d)
    assert sorted(canon - old) == sorted(DISPUTED)
    assert old - canon == set(), 'the old narrow regex saw something the owner does not'


# Each disputed doc, and what G8 does about it. Three are fixed; two are false
# positives the head window correctly refuses; two are DOCUMENT defects no regex
# can fix. 3 + 2 + 2 = 7.
FIXED_BY_G8 = {
    'references/restructure_ledger.md': 'ECOSYSTEM FILES UPDATED',
    'engine/sim_reference_CONVENTIONS.md': 'PROVISIONAL',
    'systems/combat/combat_engine_v1/README.md': 'CANONICAL',
}
FALSE_POSITIVES_REFUSED_BY_THE_WINDOW = [
    'skills/valoria-simulator/SKILL.md',
    'audit/2026-08-06-social-contest-three-lens-audit/sources/03_consolidation.md',
]
DOCUMENT_DEFECTS_NO_REGEX_CAN_FIX = [
    'workplans/valoria_master_workplan_v6.md',      # no Status line at all
    'systems/ui/valoria_ui_ux_v4.md',               # bold-wrapped `**Status:**`
]


def test_the_seven_are_partitioned_with_nothing_left_over():
    assert set(FIXED_BY_G8) | set(FALSE_POSITIVES_REFUSED_BY_THE_WINDOW) \
        | set(DOCUMENT_DEFECTS_NO_REGEX_CAN_FIX) == set(DISPUTED)
    assert len(FIXED_BY_G8) + len(FALSE_POSITIVES_REFUSED_BY_THE_WINDOW) \
        + len(DOCUMENT_DEFECTS_NO_REGEX_CAN_FIX) == 7


@pytest.mark.parametrize('doc,fragment', sorted(FIXED_BY_G8.items()))
def test_the_three_real_statuses_are_now_visible(doc, fragment):
    """GAIN direction. Each was a genuine document status that the two-hash regex
    could not see."""
    status = ci_common.doc_status(read(doc))
    assert status is not None, f'{doc} status still invisible'
    assert fragment in status.upper()


@pytest.mark.parametrize('doc', FALSE_POSITIVES_REFUSED_BY_THE_WINDOW)
def test_the_two_false_positives_stay_out(doc):
    """LOSS direction, and the reason the window is not simply widened.

    Both match the canonical pattern somewhere deep in the file — one is a schema
    template `  status : IN_FORCE | VETOED | SUPERSEDED`, the other a line far
    below the head. Neither is the document's status. The head window refuses
    them; a whole-document scan would not.
    """
    assert ci_common.doc_status(read(doc)) is None, \
        f'{doc} is now read as having a document status — the window regressed'
    assert ci_common.first_status(read(doc)) is not None, \
        f'{doc} no longer matches at all — this test is now checking nothing'


@pytest.mark.parametrize('doc', DOCUMENT_DEFECTS_NO_REGEX_CAN_FIX)
def test_the_two_document_defects_are_still_open_and_named(doc):
    """G8 does NOT close these, and saying so is the point.

    `workplans/valoria_master_workplan_v6.md` — the LIVE STEERING SURFACE — carries
    no conventional Status line at all; its currency is stated mid-sentence as
    "**2026-07-05 · status: CANON — RATIFIED**". `systems/ui/valoria_ui_ux_v4.md`
    wraps its in bold: `**Status:** CANONICAL`.

    These are content fixes in the workplans and UI lanes, not regex fixes, so an
    infrastructure step must not quietly paper over them by loosening the owner.
    When either is fixed, this test fails — which is the signal to move it into
    FIXED_BY_G8, not to relax the assertion.
    """
    assert ci_common.doc_status(read(doc)) is None, (
        f'{doc} now carries a readable Status line — move it to FIXED_BY_G8')


# ── per-reader, both directions ──────────────────────────────────────────────

def test_build_identifier_census_delta_is_plus_three_minus_one():
    """The ONE reader that moves. Both directions asserted by name."""
    import build_identifier_census as bic
    gained, lost = set(), set()
    for d in tracked_md():
        t = read(d)
        old = bool(OLD_BIC.search(t))
        new = bic.doc_status(t) is not None
        if new and not old:
            gained.add(d)
        if old and not new:
            lost.add(d)
    assert sorted(gained) == sorted(FIXED_BY_G8)
    assert sorted(lost) == ['godot/godot_architecture_specification.md']


def test_the_one_lost_document_is_a_legend_not_a_status():
    """A loss has to be justified, not just counted. This file's `## Status:` line
    reads "NOT STARTED / IN PROGRESS / COMPLETE" — a legend for a table, below the
    head. Dropping it is a fix."""
    t = read('godot/godot_architecture_specification.md')
    m = OLD_BIC.search(t)
    assert m and 'NOT STARTED' in m.group(1), 'the legend changed — re-justify the loss'
    assert t[:m.start()].count('\n') >= ci_common.STATUS_HEAD_LINES, \
        'the legend moved into the head window; it would now be read as a status'


def test_build_identifier_census_superseded_classification_is_unchanged():
    """The assertion with the real teeth. `doc_status` exists to gate a SUPERSEDED
    check that down-weights identifiers; a false positive there changes the census
    output. Zero documents change classification."""
    import build_identifier_census as bic

    def superseded(s):
        return bool(s and 'SUPERSEDED' in s.upper() and 'PART' not in s.upper())

    flips = []
    for d in tracked_md():
        t = read(d)
        m = OLD_BIC.search(t)
        before = superseded(m.group(1).strip() if m else None)
        after = superseded(bic.doc_status(t))
        if before != after:
            flips.append((d, before, after))
    assert flips == [], f'SUPERSEDED classification changed: {flips}'


def test_ci_generation_consistency_delta_is_none():
    """Its regex was ALREADY equivalent to the owner. §1.3a counted it as a
    diverging parser; it never diverged."""
    import ci_generation_consistency as cgc
    for d in tracked_md():
        t = read(d)
        old = None
        for ln in t.splitlines()[:12]:
            m = OLD_CGC.match(ln)
            if m:
                old = m.group(1).strip()
                break
        new = ci_common.first_status(t, head_lines=12)
        assert old == new, f'{d}: {old!r} -> {new!r}'
    assert callable(cgc.status_of)


def test_build_incompleteness_delta_is_none_in_its_own_scope():
    """The direction the plan explicitly warned could shrink silently.

    Measured in the feed's REAL scope (six roots), not corpus-wide — comparing a
    scoped feed against the whole corpus is the apples-to-oranges error that made
    this look like a +152 change.
    """
    import build_incompleteness as bin_
    repo = Path(ci_common.REPO)
    old, new = {}, {}
    for root in ['systems', 'engine', 'godot', 'canon', 'references', 'proposals']:
        base = repo / root
        if not base.exists():
            continue
        for md in base.rglob('*.md'):
            rel = str(md.relative_to(repo))
            if rel.startswith('deprecated/'):
                continue
            try:
                t = md.read_text(encoding='utf-8')
            except Exception:
                continue
            m = OLD_BIN.search(t)
            if m:
                old[rel] = m.group(1).upper()
            w = bin_.noncurrent_status(t)
            if w:
                new[rel] = w.upper()
    assert set(new) - set(old) == set(), f'gained: {sorted(set(new) - set(old))}'
    assert set(old) - set(new) == set(), f'LOST: {sorted(set(old) - set(new))}'
    assert {k: (old[k], new[k]) for k in old if old[k] != new[k]} == {}
    assert len(new) >= 20, 'the feed found almost nothing — it is not exercising the path'


def test_a_doc_with_two_contradictory_status_lines_is_still_reported():
    """The concrete case that made "scan every Status line" load-bearing.

    `systems/factions/faction_canon_v30.md` carries `## Status: CANONICAL` on one
    line and `## Status: PROVISIONAL — pending ratification.` on the next. A
    first-line-wins helper dropped it from the incompleteness feed. The fused
    regex it replaced did not, so neither may the composed form.
    """
    import build_incompleteness as bin_
    t = read('systems/factions/faction_canon_v30.md')
    heads = [l.strip() for l in t.splitlines()
             if ci_common.STATUS_RE.match(l.strip())]
    assert len(heads) >= 2, 'the contradictory pair was fixed — retire this test with it'
    assert bin_.noncurrent_status(t) == 'PROVISIONAL'


# ── the three corrections to §1.3a ───────────────────────────────────────────

def test_dashboard_data_has_no_independent_status_regex():
    """Correction 1: §1.3a's fifth reader does not exist.

    The `^#{1,3}\\s*Status:` pattern it attributes to dashboard_data survives ONLY
    in obs_core's comment recording what it replaced. dashboard_data consumes
    obs_core; it cannot disagree with the owner.
    """
    src = (Path(ROOT) / 'tools' / 'dashboard_data.py').read_text(encoding='utf-8')
    assert 'first_status' in src, 'dashboard_data no longer uses the shared reader'
    own = [ln for ln in src.splitlines()
           if re.search(r'Status\s*:', ln) and 're.compile' in ln]
    assert own == [], f'dashboard_data grew its own Status regex again: {own}'


def test_only_one_status_regex_is_compiled_in_the_whole_tooling_tier():
    """The recurrence guard. §1.3a's own framing is that this primitive was
    consolidated ONCE by obs_core and RE-GREW. A count assertion is what makes the
    regrowth fail a build instead of waiting for the next census."""
    owners = []
    for base in ('tools', 'skills', '.githooks'):
        for dirpath, dirnames, filenames in os.walk(os.path.join(ROOT, base)):
            dirnames[:] = [d for d in dirnames if d not in {'__pycache__', 'deprecated'}]
            for fn in filenames:
                if not fn.endswith('.py'):
                    continue
                p = os.path.join(dirpath, fn)
                for i, ln in enumerate(
                        open(p, encoding='utf-8', errors='ignore').read().splitlines(), 1):
                    if re.search(r're\.compile\([^)]*Status\s*\\?s?\*?\s*:', ln):
                        owners.append(f'{os.path.relpath(p, ROOT)}:{i}')
    assert owners == ['tools/ci_common.py:%d' % _status_re_line()], \
        f'more than one compiled Status regex in the tooling tier: {owners}'


def _status_re_line():
    src = (Path(ROOT) / 'tools' / 'ci_common.py').read_text(encoding='utf-8').splitlines()
    for i, ln in enumerate(src, 1):
        if ln.startswith('STATUS_RE = re.compile'):
            return i
    raise AssertionError('ci_common.STATUS_RE definition not found')


def test_window_choice_is_the_one_that_flips_no_superseded_classification():
    """Correction 3, and the justification for STATUS_HEAD_LINES = 80.

    The window was chosen by measuring all four candidates against the SUPERSEDED
    classification that actually consumes it:

        12 lines  -> 2 flips (two genuinely-superseded docs stop being recognised)
        40 lines  -> 0 flips
        80 lines  -> 0 flips
        whole doc -> 1 flip  (a schema template read as a status)

    40 and 80 agreeing is the stability the choice rests on. This asserts the two
    endpoints that fail, so the constant cannot drift to either without notice.
    """
    def superseded_set(window):
        out = set()
        for d in tracked_md():
            s = ci_common.first_status(read(d), head_lines=window)
            if s and 'SUPERSEDED' in s.upper() and 'PART' not in s.upper():
                out.add(d)
        return out

    at_80 = superseded_set(80)
    assert superseded_set(40) == at_80, 'the 40/80 stability that justified the constant is gone'
    assert len(superseded_set(12) ^ at_80) == 2, 'the 12-line window no longer loses two docs'
    assert len(superseded_set(None) ^ at_80) == 1, 'the whole-document false positive is gone'
    assert ci_common.STATUS_HEAD_LINES == 80
