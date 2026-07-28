"""The workflow run-discipline harness must WORK, not merely be present (ED-IN-0086).

`tools/ci_wf_harness_check.py` proves the prelude is embedded, current and called. That is a
structural check, and structural checks are exactly what §0.1 point 2 warns about: an assertion
that cannot observe the failure it excludes is not a weak test, it is an absent one. A harness
whose repetition breaker never fires, or whose `signal()` throws and kills the run it is policing,
would pass that gate cleanly.

So this module EXECUTES `tools/wf_harness.js` under node and drives each discipline to its failure
mode. It runs against the OWNER, because the owner is the only editable copy and the checker
already proves the copies are byte-identical to it.

Node is required. On a machine without it these tests skip — visibly, in the pytest summary — and
the structural gate still runs. GitHub's ubuntu-latest images ship node, so CI executes them.
"""
import json
import os
import shutil
import subprocess
import textwrap

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
OWNER = os.path.join(ROOT, 'tools', 'wf_harness.js')
BEGIN = "// ==== VALORIA WF HARNESS v1 — GENERATED FROM tools/wf_harness.js — DO NOT EDIT HERE ===="
END = "// ==== END VALORIA WF HARNESS v1 ===="

NODE = shutil.which('node')
needs_node = pytest.mark.skipif(
    NODE is None,
    reason="node not installed — the harness is JavaScript and cannot be executed here. The "
           "structural gate (tools/ci_wf_harness_check.py) still runs; these behavioural "
           "assertions do not.")


def _harness_source():
    with open(OWNER, encoding='utf-8') as fh:
        text = fh.read()
    i, j = text.find(BEGIN), text.find(END)
    assert i >= 0 and j >= 0, "tools/wf_harness.js has lost its sentinels"
    return text[i:j + len(END)]


def run_js(body):
    """Execute the harness plus `body`, returning whatever body JSON-prints on the last line.

    `log` is stubbed: in the sandbox it is a workflow global, and the harness calls it from
    signal(). Stubbing it is also the point — a harness that only works when log() exists would
    be a hidden coupling.
    """
    src = "const log = () => {};\n" + _harness_source() + "\n" + textwrap.dedent(body)
    r = subprocess.run([NODE, '--input-type=module', '-e', src],
                       capture_output=True, text=True, timeout=60)
    assert r.returncode == 0, f"node exited {r.returncode}\nSTDERR:\n{r.stderr}\nSTDOUT:\n{r.stdout}"
    out = [ln for ln in r.stdout.strip().splitlines() if ln.strip()]
    assert out, f"script printed nothing\nSTDERR:\n{r.stderr}"
    return json.loads(out[-1])


# ─────────────────────────────────────────────────────────── P3 · termination discipline

@needs_node
def test_a_clean_run_reports_completed_and_is_not_degraded():
    """The baseline. Without it, every assertion below could pass on a harness that always alarms."""
    s = run_js("""
        const run = hRun('clean')
        run.lens('a', [{ claim: 'x is dead', evidence: 'a.py:1' }])
        console.log(JSON.stringify(run.summary()))
    """)
    assert s['stop_reason'] == 'completed'
    assert s['degraded'] is False
    assert s['signals'] == []


@needs_node
def test_round_cap_signals_but_the_run_continues():
    """REPORT-ONLY IS THE RULING (Jordan, 2026-07-28). Past the cap the run keeps going.

    This is the assertion that would catch a future 'improvement' that makes the breaker throw or
    return early — which is what the upstream precedent does, and what was deliberately not copied.
    """
    s = run_js("""
        const run = hRun('capped')
        let reached = 0
        for (let i = 0; i < 6; i++) { run.round('r' + i, [{ claim: 'c' + i, evidence: 'f' + i + '.py:1' }]); reached = i }
        console.log(JSON.stringify(Object.assign(run.summary(), { reached })))
    """)
    assert s['reached'] == 5, "the loop stopped early — the breaker is not report-only"
    assert s['rounds'] == 6
    assert s['stop_reason'] == 'round_cap'
    assert s['degraded'] is True
    assert sum(1 for x in s['signals'] if x['reason'] == 'round_cap') == 3, \
        "expected one round_cap signal per round past the cap of 3"


@needs_node
def test_repetition_fires_only_when_a_round_repeats_the_previous_one():
    """Both directions. A breaker that fires on everything is as useless as one that never fires."""
    repeated = run_js("""
        const run = hRun('thrash')
        const same = [{ claim: 'reach is over-weighted', evidence: 'combat_systems.py:11' }]
        run.round('r1', same)
        run.round('r2', same)
        console.log(JSON.stringify(run.summary()))
    """)
    assert repeated['stop_reason'] == 'repetition'

    progressing = run_js("""
        const run = hRun('progress')
        run.round('r1', [{ claim: 'reach is over-weighted', evidence: 'combat_systems.py:11' }])
        run.round('r2', [{ claim: 'tempo is compressed away', evidence: 'wrapper.py:66' }])
        console.log(JSON.stringify(run.summary()))
    """)
    assert progressing['stop_reason'] == 'completed', \
        "a round that found something new tripped the repetition breaker"


@needs_node
def test_an_empty_round_is_not_repetition():
    """Two rounds of nothing is a null-result problem, not a thrash problem, and conflating them
    would attribute the wrong cause in the summary a human reads."""
    s = run_js("""
        const run = hRun('empty')
        run.round('r1', [])
        run.round('r2', [])
        console.log(JSON.stringify(run.summary()))
    """)
    assert s['stop_reason'] == 'completed'


@needs_node
def test_signal_never_throws_even_on_an_unknown_reason():
    """The harness must not be able to kill the run it polices. An out-of-set reason is recorded
    as `invalid_signal` — loud, representable, non-fatal."""
    s = run_js("""
        const run = hRun('bad-signal')
        run.signal('made_up_reason', 'from a future edit')
        console.log(JSON.stringify(run.summary()))
    """)
    assert s['stop_reason'] == 'invalid_signal'
    assert s['signals'][0]['requested'] == 'made_up_reason'


@needs_node
def test_the_summary_survives_every_signal_at_once():
    """A run that tripped everything still returns a complete report — the whole point of
    report-only. If this ever fails, the harness has started swallowing results."""
    s = run_js("""
        const run = hRun('everything')
        const same = [{ claim: 'x', evidence: 'a.py:1' }]
        run.lens('silent', [])
        run.critiqued('stage', 10, 3)
        run.dispute({ finding_id: 'F1', layer_disputed: 'evidence', root_cause: 'stale-canon' })
        for (let i = 0; i < 5; i++) run.round('r' + i, same)
        console.log(JSON.stringify(run.summary()))
    """)
    assert s['degraded'] is True
    reasons = {x['reason'] for x in s['signals']}
    assert {'null_result', 'critic_starved', 'repetition', 'round_cap',
            'disagreement_unadjudicated'} <= reasons
    assert s['stop_reason'] == 'round_cap', "precedence should surface the worst signal"
    assert s['trace_jsonl'], "the run trace is empty — nothing to reconstruct the run from"
    for line in s['trace_jsonl'].splitlines():
        json.loads(line)   # every trace line must be valid JSON, or it is not a JSONL trace


# ─────────────────────────────────────────────────────── P7 · null result + rediscovery

@needs_node
def test_null_result_alarm_fires_on_an_empty_lens_and_not_on_a_full_one():
    s = run_js("""
        const run = hRun('lenses')
        run.lens('found-nothing', [])
        run.lens('found-something', [{ claim: 'a', evidence: 'x.md:1' }])
        console.log(JSON.stringify(run.summary()))
    """)
    nulls = [x for x in s['signals'] if x['reason'] == 'null_result']
    assert len(nulls) == 1
    assert 'found-nothing' in nulls[0]['detail']


@needs_node
def test_rediscovery_counts_distinct_lenses_not_findings():
    """The corroboration signal. One lens repeating itself must NOT look like corroboration —
    that is the failure mode that would make the whole ranking worthless."""
    s = run_js("""
        const f = (claim, evidence, lens) => ({ claim, evidence, lens })
        const ranked = hRediscover([
          f('the persuasion track collapses four games', 'social_contest_v30.md:40', 'four-games'),
          f('persuasion track collapses the four games into one bar', 'social_contest_v30.md:212', 'caillois'),
          f('one persuasion track collapses four different games', 'social_contest_v30.md:9', 'meta-game'),
          f('no commitment store exists', 'social_contest_v30.md:88', 'commitment-store'),
          f('no commitment store exists', 'social_contest_v30.md:88', 'commitment-store'),
        ], (x) => x.lens)
        console.log(JSON.stringify(ranked))
    """)
    top = s[0]
    assert top['rediscovery'] == 3
    assert sorted(top['lenses']) == ['caillois', 'four-games', 'meta-game']
    selfdup = [g for g in s if g['rediscovery'] == 1]
    assert selfdup, "the twice-reported single-lens finding should rank 1, not 2"
    assert selfdup[0]['lenses'] == ['commitment-store']
    assert len(selfdup[0]['findings']) == 2, "both copies should still be carried, just not counted twice"


@needs_node
def test_rediscovery_keys_on_the_file_not_the_line():
    """Two lenses describing one defect cite lines a few apart. Keying on `file:line` would split
    every rediscovered defect into singletons and silently zero out the whole signal."""
    s = run_js("""
        const ranked = hRediscover([
          { claim: 'dead geo coefficients are never consumed', evidence: 'geometry.py:41', lens: 'A' },
          { claim: 'the geo coefficients are dead, never consumed', evidence: 'geometry.py:88', lens: 'B' },
        ], (x) => x.lens)
        console.log(JSON.stringify(ranked))
    """)
    assert s[0]['rediscovery'] == 2, "line numbers leaked into the rediscovery key"


@needs_node
def test_rediscovery_reads_both_finding_shapes_in_this_repo():
    """The combat/attribute shape puts citations in free-text `evidence`; the social-contest shape
    puts them in `locations[].file`. One normalizer has to read both or the ranking is blind to
    whichever workflow it was not written against."""
    s = run_js("""
        const ranked = hRediscover([
          { claim: 'adjudicator is a flat resistance scalar', locations: [{ file: 'engine/params/contest.md', quote: 'q' }], lens: 'A' },
          { claim: 'the adjudicator is only a flat scalar resistance', evidence: 'engine/params/contest.md:120', lens: 'B' },
        ], (x) => x.lens)
        console.log(JSON.stringify(ranked))
    """)
    assert s[0]['rediscovery'] == 2, "the two finding shapes did not normalize to one key"


# ────────────────────────────────────────────────────────── P8 · disagreement records

@needs_node
def test_an_unadjudicated_dispute_reaches_the_summary_as_a_signal():
    """No silent disappearance. This is the whole of P8: a dispute nobody ruled on must be visible
    in the returned summary, by name."""
    s = run_js("""
        const run = hRun('disputes')
        run.dispute({ finding_id: 'C1:F3', layer_disputed: 'severity', root_cause: 'severity-calibration' })
        console.log(JSON.stringify(run.summary()))
    """)
    assert s['stop_reason'] == 'disagreement_unadjudicated'
    assert s['unadjudicated'] == ['C1:F3']


@needs_node
def test_adjudication_clears_the_signal_and_an_empty_ruling_does_not():
    s = run_js("""
        const a = hRun('ruled')
        a.dispute({ finding_id: 'F1', layer_disputed: 'evidence', root_cause: 'stale-canon' })
        a.adjudicate('F1', 'critic-holds: the cited line was superseded by ED-1085', 'synthesis')
        const b = hRun('empty-ruling')
        b.dispute({ finding_id: 'F2', layer_disputed: 'evidence', root_cause: 'stale-canon' })
        b.adjudicate('F2', '', 'synthesis')
        console.log(JSON.stringify({ ruled: a.summary(), empty: b.summary() }))
    """)
    assert s['ruled']['stop_reason'] == 'completed'
    assert s['ruled']['disagreements'][0]['status'] == 'resolved'
    assert s['empty']['stop_reason'] == 'disagreement_unadjudicated', \
        "an empty ruling counted as an adjudication — that is a silent disappearance with extra steps"


@needs_node
def test_cross_domain_records_are_observations_and_cannot_be_ruled_on():
    """Observe, do not judge. An out-of-lane record must not block the run AND must not be
    overwritable by a later ruling — a confident verdict on someone else's lane from a partial
    read is exactly what this rule exists to stop."""
    s = run_js("""
        const run = hRun('cross-domain')
        run.dispute({ finding_id: 'C4:conformance', layer_disputed: 'scope', root_cause: 'scope-boundary', cross_domain: true })
        const n = run.adjudicate('C4:conformance', 'IN-lane rules it out of scope', 'synthesis')
        console.log(JSON.stringify(Object.assign(run.summary(), { adjudicated: n })))
    """)
    assert s['adjudicated'] == 0, "an observation was adjudicated"
    d = s['disagreements'][0]
    assert d['status'] == 'observation'
    assert d['adjudication'] == '', "a ruling overwrote an out-of-lane observation"
    assert s['stop_reason'] == 'completed', "an observation should not read as an unruled dispute"


@needs_node
def test_out_of_vocabulary_layer_and_root_cause_fall_back_instead_of_throwing():
    """Closed vocabularies, enforced by normalization rather than by an exception — a workflow
    stage passing a typo'd root cause must not take the run down with it."""
    s = run_js("""
        const run = hRun('bad-vocab')
        const d = run.dispute({ finding_id: 'F1', layer_disputed: 'vibes', root_cause: 'because' })
        run.adjudicate('F1', 'x', 'y')
        console.log(JSON.stringify(d))
    """)
    assert s['layer_disputed'] in ('evidence', 'interpretation', 'severity', 'scope', 'method')
    assert s['root_cause'] in ('different-sources-read', 'stale-canon', 'ambiguous-spec',
                               'severity-calibration', 'scope-boundary', 'measurement-vs-assertion')


# ──────────────────────────────────────────────────── P4 · structurally read-only critics

@needs_node
def test_hcritic_sets_the_agent_type_and_preserves_the_callers_options():
    s = run_js("""
        console.log(JSON.stringify(hCritic({ label: 'verify:x', phase: 'Verify', model: 'sonnet' })))
    """)
    assert s['agentType'] == 'valoria-critic'
    assert s['label'] == 'verify:x' and s['phase'] == 'Verify' and s['model'] == 'sonnet'


def test_the_critic_agent_definition_grants_no_write_tools():
    """The one assertion here that does not need node, because it is the load-bearing one: P4's
    entire claim is that critic independence is structural. If this file ever grants Write, Edit
    or Bash, `hCritic()` becomes the same display string it replaced."""
    path = os.path.join(ROOT, '.claude', 'agents', 'valoria-critic.md')
    assert os.path.exists(path), "the read-only critic agent definition is missing"
    with open(path, encoding='utf-8') as fh:
        head = fh.read().split('---')[1]
    tools = [t.strip() for t in
             next(l.split(':', 1)[1] for l in head.splitlines() if l.startswith('tools:')).split(',')]
    assert tools, "no tools declared — an empty list inherits everything, including Write"
    assert not (set(tools) & {'Write', 'Edit', 'NotebookEdit', 'Bash', 'Artifact'}), \
        f"the critic can write: {tools}"


def test_every_workflow_embeds_the_owner_byte_for_byte():
    """Guards the copies without re-implementing the checker's rule: it asserts the same identity
    the gate asserts, so a drifted copy fails here too rather than only in CI."""
    import glob
    block = _harness_source()
    scripts = sorted(glob.glob(os.path.join(ROOT, '.claude', 'wf_*.js')))
    assert scripts, "no .claude/wf_*.js found — this test would pass vacuously"
    checked = 0
    for path in scripts:
        with open(path, encoding='utf-8') as fh:
            text = fh.read()
        i, j = text.find(BEGIN), text.find(END)
        assert i >= 0 and j >= 0, f"{os.path.basename(path)} carries no harness block"
        assert text[i:j + len(END)] == block, (
            f"{os.path.basename(path)} has drifted from tools/wf_harness.js — the owner is the only "
            f"editable copy; re-sync with `python tools/ci_wf_harness_check.py --fix`")
        checked += 1
    assert checked == len(scripts)
