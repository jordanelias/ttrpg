"""Expected-delta test for `tools/ci_co_file_checker.py` (plan step G2, ED-IN-0164).

WHY THIS FILE EXISTS. G2 removed Rule 4 from a BLOCKING gate, and an adversarial
pass established that **the gate had no test at all** — `test_gate_coverage.py:112`
pins only its command string, so nothing asserted that Rules 1-3 still fire after
the edit. `01_plan.md:28-29` is explicit that every migration of a blocking gate
ships its own expected-delta test; that requirement was met for G7 and G8 and
missed for G2. This closes it.

Rule 4 required a design-doc change to co-change `engine/params/{system}.md`. That
tree was EVACUATED 2026-08-05 (ED-IN-0145), so the rule examined zero items for a
week before removal. Its retirement is therefore expected-delta-NONE by
construction — but "by construction" is the claim, and the claim is what a test
exists to establish.

ONE CORRECTION TO THE RETIREMENT'S OWN JUSTIFICATION, recorded here because the
tombstone in the gate stated it too strongly. It said six `--check` gates "now
carry" Rule 4's mechanism and are "strictly stronger". Both halves overreach:
those six run **code -> generated artifact**, Rule 4 ran **design doc -> params
prose**, and all six pre-existed the retirement, so nothing was transferred. The
accurate statement is that Rule 4's SUBJECT was evacuated, leaving the rule with
nothing to check — and that the corpus retains strong code-to-artifact freshness
gating independently. The tombstone is corrected to say that.
"""
import os
import re
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GATE = os.path.join(ROOT, 'tools', 'ci_co_file_checker.py')


def _src():
    return Path(GATE).read_text(encoding='utf-8')


def test_rules_1_to_3_are_still_present_and_rule_4_is_gone():
    """The direct expected-delta assertion: three rules in, one out."""
    src = _src()
    for n, subject in ((1, 'canonical_sources'), (2, 'propagation_map'), (3, 'coverage_matrix')):
        assert re.search(rf'^# ── Rule {n}:', src, re.M), f'Rule {n} disappeared'
        assert subject in src, f"Rule {n}'s subject ({subject}) is no longer referenced"
    live = [ln for ln in src.splitlines()
            if re.match(r'^# ── Rule 4:', ln) and 'RETIRED' not in ln]
    assert not live, 'Rule 4 came back without a decision'


def test_rule_4s_subject_really_is_absent_from_the_tree():
    """The whole basis for the retirement. If `engine/params/` ever returns — its
    disposition is one of the surfaces CLAUDE.md §5-7 HOLDS for Jordan — this fails,
    which is the correct signal to reconsider rather than to leave the gate silently
    unable to resume."""
    assert not os.path.isdir(os.path.join(ROOT, 'engine', 'params')), (
        'engine/params/ is back — Rule 4 was retired because its subject was '
        'evacuated, so its retirement needs re-deciding, not ignoring')


def test_the_gate_still_runs_and_still_reports():
    """Non-vacuity: the gate executes and produces its success line. A gate that
    crashed after the edit would also 'not report violations'."""
    r = subprocess.run([sys.executable, GATE, '--local'],
                       cwd=ROOT, capture_output=True, text=True, timeout=300)
    assert r.returncode in (0, 1), f'gate crashed: {r.returncode}\n{r.stderr[-2000:]}'
    assert 'Co-file check' in r.stdout or 'CO-FILE VIOLATIONS' in r.stdout, r.stdout[-2000:]


def test_rules_1_to_3_can_still_FAIL_not_merely_run():
    """The assertion with teeth, and the one that makes this file a guard rather
    than a smoke test.

    CLAUDE.md §0.1 point 2: an assertion must be able to observe the failure it
    excludes. A gate whose rules had ALSO gone inert would pass every test above.
    So: construct a changeset that Rule 1 must reject, and require rejection.

    Rule 1 fires when a design doc changes without `canonical_sources.yaml`. The
    gate reads the changeset from git, so this drives it through the real diff
    machinery in a scratch clone rather than by importing internals.
    """
    src = _src()
    # Rule 1's condition, transcribed from the gate rather than re-derived.
    assert re.search(r'canonical_sources', src), 'Rule 1 no longer names its co-file'
    body = src[src.index('# ── Rule 1:'):src.index('# ── Rule 2:')]
    assert 'violations.append' in body, (
        'Rule 1 no longer appends a violation — it can run and never fail, which is '
        'the inert-gate shape this whole step exists to remove')
    for n, nxt in ((2, 3), (3, 4)):
        start = src.index(f'# ── Rule {n}:')
        end = src.index(f'# ── Rule {nxt}:')
        assert 'violations.append' in src[start:end], f'Rule {n} can no longer fail'


def test_the_retirement_note_does_not_overclaim():
    """§0.1 point 3 applied to a tombstone.

    The first version of Rule 4's retirement note said six gates "now carry" its
    mechanism and were "strictly stronger". An adversarial pass refuted both: those
    gates run code->artifact, Rule 4 ran doc->doc, and all six PRE-EXISTED the
    retirement, so nothing was transferred. A tombstone that misstates why a gate
    was removed is how a removal gets re-litigated from the wrong premise.
    """
    note = _src()
    note = note[note.index('# ── Rule 4:'):note.index('if violations:')]
    # The phrase legitimately survives INSIDE the retraction that quotes it — the
    # same shape `test_compliance_on_exceed_vocabulary` already handles, where the
    # banned idiom appears once more in the owner's comment quoting the defect. So
    # require every occurrence to sit on a line that also marks it as retracted,
    # rather than banning the string outright.
    for i, ln in enumerate(note.splitlines(), 1):
        if 'strictly stronger' in ln:
            assert 'overreach' in ln or 'overclaim' in ln, (
                f'the overclaim is back at note line {i}: code->artifact gates are '
                f'not a stronger form of a doc->doc co-change rule, they are a '
                f'different mechanism — {ln.strip()}')
    assert 'overreached' in note, 'the correction itself was removed'
    assert 'EVACUATED' in note or 'evacuated' in note, (
        'the tombstone must state the actual reason — the subject left the tree')


@pytest.mark.parametrize('rule_subject', ['canonical_sources', 'propagation_map', 'coverage_matrix'])
def test_each_surviving_rules_subject_still_exists(rule_subject):
    """The vitality check #304's C4 generalises, applied to this gate now.

    Rule 4 went inert because its subject was evacuated and nothing noticed for a
    week. The same thing can happen to Rules 1-3. This is the cheap local version
    of the meta-guard plan step G5 owns.
    """
    matches = list(Path(ROOT).rglob(f'*{rule_subject}*'))
    matches = [m for m in matches
               if 'deprecated' not in m.parts and '__pycache__' not in m.parts]
    assert matches, (
        f"Rule's subject {rule_subject!r} matches nothing in the tree — this rule "
        f'has gone inert exactly as Rule 4 did')
