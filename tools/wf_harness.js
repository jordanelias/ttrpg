// VALORIA WF HARNESS — the single owner of the run-discipline prelude embedded in .claude/wf_*.js
// ---------------------------------------------------------------------------------------------
// WHY A GENERATED COPY INSTEAD OF AN IMPORT. Claude Code workflow scripts run in a sandbox with
// no filesystem and no Node API, so `require`/`import` is not available to them. CLAUDE.md §8's
// invariant ("every rule lives once") still has to hold, so the rule lives HERE and is copied
// verbatim into each script between sentinels. `tools/ci_wf_harness_check.py` fails if any copy
// has drifted, and `--fix` re-syncs them. Editing a copy in .claude/ is the thing the checker is
// built to catch; edit this file.
//
// WHAT IT IS FOR (ED-IN-0087, executing P3/P4/P7/P8 of ED-IN-0085's report). The .claude/
// workflows were strong at fanning out and at adversarial refutation, and had no mechanism at
// all for: knowing when to stop (P3), forcing critic independence (P4), noticing that a critic
// found nothing (P7), or recording a disagreement it then failed to resolve (P8).
//
// BESPOKE, NOT IMPORTED. Two precedents were read — itsmesherry/claude-audit's repetition
// breaker and ChristopherKahler/aegis's disagreement record — and neither was ported. Their
// shapes assume production software with CVEs, deploy gates and liability tiers; this is a
// solo design repo whose findings carry `file:line` evidence and a P1/P2/P3 or high/medium/low
// weight, whose critics are a stateless relay stage, and whose lenses are named. Every
// normalizer below keys on THOSE fields.
//
// REPORT-ONLY BY RULING (Jordan, 2026-07-28: "P3 report-only"). Nothing here aborts a run.
// Every signal is recorded, surfaced in the returned summary, and the workflow CONTINUES. A
// breaker that halts a 40-agent audit on a heuristic costs more than the defect it caught, and
// a silent halt is worse than a noisy completion. The falsifier for that choice is explicit:
// tests/valoria/test_wf_harness.py asserts hRun().signal() never throws and that a run which
// tripped every signal still returns a full summary.

// ==== VALORIA WF HARNESS v1 — GENERATED FROM tools/wf_harness.js — DO NOT EDIT HERE ====
// Re-sync after editing the owner:  python tools/ci_wf_harness_check.py --fix
// Report-only by ruling (Jordan 2026-07-28): every signal records and the run CONTINUES.

// P3 · the closed set. A reason outside it is itself a defect, representable without throwing.
const H_STOP_REASONS = [
  'completed',                   // nothing fired
  'null_result',                 // P7: a lens/critic returned zero findings
  'critic_starved',              // a stage produced findings that no critic ever saw
  'disagreement_unadjudicated',  // P8: a dispute reached the return with no ruling
  'repetition',                  // P3: a round reproduced the previous round's finding set
  'round_cap',                   // P3: the loop hit its cap
  'invalid_signal',              // a caller passed a reason outside this set
]
// Reported stop_reason = the worst signal seen, ordered by how much it should make a READER
// distrust the run — not by the severity of any underlying finding.
const H_STOP_RANK = H_STOP_REASONS
const H_ROUND_CAP = 3

// P8 · closed vocabularies for a disagreement. Deliberately small; each value is a distinction
// this repo's critics actually draw (see the uphold/overturn/soften/sharpen funnel).
const H_DISPUTE_LAYERS = ['evidence', 'interpretation', 'severity', 'scope', 'method']
const H_ROOT_CAUSES = [
  'different-sources-read',     // agonist and critic opened different files
  'stale-canon',               // one side read a superseded head
  'ambiguous-spec',            // the doc genuinely admits both readings
  'severity-calibration',      // same facts, different weight
  'scope-boundary',            // in-lane vs out-of-lane, or in-scope vs out-of-scope
  'measurement-vs-assertion',  // one side measured, the other asserted
]

// The cross-lens identity of a finding (P7's rediscovery key, P3's repetition key).
// Bespoke: two lenses that independently hit one defect cite the SAME FILE and describe it in
// different words, usually a line or two apart — so the key is (first cited file path, line
// dropped) + the first content words of the claim. Line numbers are dropped on purpose; keeping
// them would split one rediscovered defect into N singletons, which is the failure this exists
// to prevent.
const H_STOPWORDS = ['the', 'a', 'an', 'is', 'are', 'was', 'were', 'and', 'or', 'but', 'of', 'to',
  'in', 'on', 'at', 'for', 'with', 'that', 'this', 'it', 'its', 'as', 'by', 'from', 'has', 'have',
  'not', 'no', 'be', 'been', 'does', 'do', 'never', 'only', 'any']

function hClaimText(f) {
  if (!f || typeof f !== 'object') return ''
  return String(f.claim || f.title || f.what || f.summary || '')
}

function hFirstFile(f) {
  if (!f || typeof f !== 'object') return ''
  // social-contest shape: locations[{file, quote}]
  if (Array.isArray(f.locations) && f.locations.length && f.locations[0] && f.locations[0].file) {
    return String(f.locations[0].file).split(':')[0].trim()
  }
  // combat / attribute shape: `evidence` is free-text "file:line" citations
  const src = String(f.evidence || f.surface || f.defining_surface || '')
  const m = src.match(/[A-Za-z0-9_./-]+\.(?:md|py|ya?ml|json|jsonl|gd|js|html)/)
  return m ? m[0] : ''
}

function hContentWords(f) {
  const seen = []
  for (const w of hClaimText(f).toLowerCase().replace(/[^a-z0-9\s]/g, ' ').split(/\s+/)) {
    if (w.length > 2 && H_STOPWORDS.indexOf(w) < 0 && seen.indexOf(w) < 0) seen.push(w)
  }
  return seen
}

// The EXACT key: same file, same claim wording. Used by the repetition breaker, where the question
// is "did this stage produce literally the same output again", so exactness is what is wanted.
function hFindingKey(f) {
  return (hFirstFile(f) || '?') + '#' + (hContentWords(f).slice(0, 6).join('-') || '?')
}

// The FUZZY match, used only by rediscovery. Two lenses that independently hit one defect describe
// it in different words — "dead geo coefficients are never consumed" and "the geo coefficients are
// dead, never consumed" are one finding. An exact key splits them into singletons and silently
// zeroes out the entire corroboration signal, which is worse than not computing it: the output
// still has a `rediscovery` column, it just always reads 1.
// So: same file, and one claim's content words substantially contained in the other's.
// Containment, not Jaccard — a thorough lens writes a longer sentence about the same defect, and
// Jaccard punishes exactly that. The absolute floor stops a two-word claim matching everything.
function hSameFinding(a, b) {
  if (hFirstFile(a) !== hFirstFile(b)) return false
  const wa = hContentWords(a), wb = hContentWords(b)
  if (!wa.length || !wb.length) return false
  const shared = wa.filter(w => wb.indexOf(w) >= 0).length
  const smaller = Math.min(wa.length, wb.length)
  if (smaller < 3) return shared === smaller && wa.length === wb.length
  return shared >= 3 && shared / smaller >= 0.6
}

// P3 · the run recorder. One per workflow; every stage reports through it.
function hRun(name) {
  const run = {
    name: name,
    rounds: 0,
    cap: H_ROUND_CAP,
    signals: [],          // append-only; nothing is ever removed (no-silent-disappearance)
    trace: [],            // the JSONL run trace, emitted by hSummary()
    disagreements: [],
    _lastRoundKeys: null,
  }

  run.trace_ = function (event, data) {
    run.trace.push(Object.assign({ seq: run.trace.length, event: event }, data || {}))
    return run
  }

  // NEVER throws. An unknown reason is recorded as 'invalid_signal' carrying what was asked for,
  // because a harness that crashes the run it is policing is worse than the drift it detects.
  run.signal = function (reason, detail) {
    const known = H_STOP_REASONS.indexOf(reason) >= 0 && reason !== 'completed'
    const rec = { reason: known ? reason : 'invalid_signal', detail: String(detail || ''), round: run.rounds }
    if (!known) rec.requested = String(reason)
    run.signals.push(rec)
    run.trace_('signal', rec)
    log('[harness] ' + rec.reason + ': ' + rec.detail)
    return run
  }

  // Round accounting + the repetition breaker. Report-only: past the cap it still returns true
  // and the caller decides; the SIGNAL is the deliverable, not a forced exit.
  run.round = function (label, findings) {
    run.rounds += 1
    const keys = Array.isArray(findings) ? findings.map(hFindingKey).sort() : null
    run.trace_('round', { label: String(label || ''), n: run.rounds, findings: keys ? keys.length : 0 })
    if (run.rounds > run.cap) {
      run.signal('round_cap', 'round ' + run.rounds + ' exceeds cap ' + run.cap + ' (' + label + ')')
    }
    if (keys && run._lastRoundKeys && keys.length && keys.join('|') === run._lastRoundKeys.join('|')) {
      run.signal('repetition', 'round ' + run.rounds + ' (' + label + ') reproduced the previous round\'s '
        + keys.length + ' finding(s) with no change — further rounds are unlikely to add anything')
    }
    if (keys) run._lastRoundKeys = keys
    return run
  }

  // P7a · the null-result alarm. Ships with hRediscover (P7b) and is meaningless without it:
  // an alarm for "you found nothing" with no way to see WHICH findings were corroborated is
  // pressure to manufacture findings. Both are called in every script; the checker enforces it.
  run.lens = function (lensKey, findings) {
    const n = Array.isArray(findings) ? findings.length : 0
    run.trace_('lens', { lens: String(lensKey), findings: n })
    if (n === 0) {
      run.signal('null_result', 'lens/stage "' + lensKey + '" returned zero findings — either the '
        + 'surface is genuinely clean, or the agent failed to read it. Check its coverage notes '
        + 'before crediting the silence.')
    }
    return findings || []
  }

  // A stage produced findings that no critic ever saw. The relay is the method (CLAUDE.md §10);
  // an unrefuted finding is a draft, not a result.
  run.critiqued = function (stage, produced, reviewed) {
    run.trace_('critique-coverage', { stage: String(stage), produced: produced, reviewed: reviewed })
    if (produced > 0 && reviewed < produced) {
      run.signal('critic_starved', stage + ': ' + reviewed + '/' + produced + ' finding(s) reached a '
        + 'critic; ' + (produced - reviewed) + ' returned unrefuted')
    }
    return run
  }

  // P8 · a disagreement record. `adjudication` starts empty ON PURPOSE — hSummary() signals if
  // it is still empty at the return, which is the no-silent-disappearance rule.
  run.dispute = function (rec) {
    const d = {
      finding_id: String((rec && rec.finding_id) || '?'),
      layer_disputed: H_DISPUTE_LAYERS.indexOf(rec && rec.layer_disputed) >= 0 ? rec.layer_disputed : 'interpretation',
      positions: (rec && rec.positions) || [],
      root_cause: H_ROOT_CAUSES.indexOf(rec && rec.root_cause) >= 0 ? rec.root_cause : 'ambiguous-spec',
      resolution_model: (rec && rec.resolution_model) || 'adjudicated-by-synthesis',
      cross_domain: !!(rec && rec.cross_domain),
      adjudication: '',
      status: 'open',
    }
    // CROSS-DOMAIN OBSERVATION, NOT JUDGMENT: a critic reaching outside its own lens/lane may
    // report what it saw but may not rule on it. Encoded, not merely asked for — the record
    // cannot leave this branch in a state that a later ruling would silently overwrite.
    if (d.cross_domain) {
      d.status = 'observation'
      d.resolution_model = 'observation-only (out-of-lens: report, do not rule)'
    }
    run.disagreements.push(d)
    run.trace_('dispute', { finding_id: d.finding_id, layer: d.layer_disputed, root_cause: d.root_cause, cross_domain: d.cross_domain })
    return d
  }

  run.adjudicate = function (findingId, ruling, by) {
    let n = 0
    for (const d of run.disagreements) {
      if (d.finding_id !== String(findingId) || d.status === 'observation') continue
      d.adjudication = String(ruling || '')
      d.adjudicated_by = String(by || 'synthesis')
      d.status = d.adjudication ? 'resolved' : 'open'
      n += d.status === 'resolved' ? 1 : 0
    }
    run.trace_('adjudicate', { finding_id: String(findingId), resolved: n })
    return n
  }

  run.summary = function () {
    const unadj = run.disagreements.filter(d => d.status === 'open')
    if (unadj.length) {
      run.signal('disagreement_unadjudicated', unadj.length + ' dispute(s) reached the return with no '
        + 'ruling: ' + unadj.map(d => d.finding_id).join(', '))
    }
    let worst = 'completed'
    for (const s of run.signals) {
      if (H_STOP_RANK.indexOf(s.reason) > H_STOP_RANK.indexOf(worst)) worst = s.reason
    }
    return {
      run: run.name,
      stop_reason: worst,
      degraded: worst !== 'completed',
      rounds: run.rounds,
      round_cap: run.cap,
      signals: run.signals,
      disagreements: run.disagreements,
      unadjudicated: unadj.map(d => d.finding_id),
      trace_jsonl: run.trace.map(t => JSON.stringify(t)).join('\n'),
    }
  }

  return run
}

// P7b · rank by INDEPENDENT REDISCOVERY. Practice 7 (one agent per lens) already produces this
// signal and every script threw it away. A defect three unrelated lenses hit independently is
// worth more than one a single lens hit hard, and this is the only cheap corroboration signal a
// read-only audit has. `lensOf` extracts the lens/cluster key so a lens cannot corroborate itself.
function hRediscover(findings, lensOf) {
  const groups = []
  for (const f of (findings || [])) {
    if (!f) continue
    const lens = String((lensOf && lensOf(f)) || f.lens || f.cluster || f.module || '?')
    let g = null
    for (const cand of groups) {
      if (hSameFinding(cand.findings[0], f)) { g = cand; break }
    }
    if (!g) { g = { key: hFindingKey(f), lenses: [], findings: [] }; groups.push(g) }
    if (g.lenses.indexOf(lens) < 0) g.lenses.push(lens)
    g.findings.push(f)
  }
  return groups
    .map(g => ({ key: g.key, rediscovery: g.lenses.length, lenses: g.lenses, findings: g.findings }))
    .sort((a, b) => b.rediscovery - a.rediscovery || a.key.localeCompare(b.key))
}

// P4 · the read-only critic. Independence is STRUCTURAL, not a sentence in a prompt: the
// agentType below is defined in .claude/agents/valoria-critic.md with a tools list that has no
// Write/Edit. Passing it is the whole mechanism — a critic stage that omits it can write, and
// tools/ci_wf_harness_check.py fails the script that does.
const H_CRITIC = { agentType: 'valoria-critic' }
function hCritic(opts) { return Object.assign({}, opts || {}, H_CRITIC) }
// ==== END VALORIA WF HARNESS v1 ====
