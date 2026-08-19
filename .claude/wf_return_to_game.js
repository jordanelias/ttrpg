export const meta = {
  name: 'return-to-game',
  description: 'Executes ONE step of workplans/return_to_game_queue.yaml under staged adversarial review. Pass the step id as args (e.g. "S1"). Produces the work, then puts three structurally read-only critics on it — fidelity, factuality, logic — and returns a verdict the caller commits or reverts. No step blocks on a human.',
  phases: [
    { title: 'Orient', detail: 'read the queue, load the step, verify its precondition still holds on disk', model: 'sonnet' },
    { title: 'Produce', detail: 'execute the step in an isolated worktree; run its own gate; return artifacts and claims', model: 'sonnet' },
    { title: 'Critique', detail: 'three read-only valoria-critic lanes over the artifacts only — fidelity, factuality, logic', model: 'opus' },
    { title: 'Reconcile', detail: 'adjudicate verdicts; overturn blocks the commit; return the queue patch', model: 'opus' },
  ],
}

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

  // A CRITIC THAT DIED IS NOT A CRITIC THAT FOUND NOTHING, and the scripts could not tell them
  // apart. The pipeline pattern is `.then(v => ({...f, verdict: v})).catch(() => null)` followed by
  // `.filter(Boolean)` — so a critic that errors drops the WHOLE FINDING, and the obvious coverage
  // check (`produced = survivors.length`) then compares a set to itself and can never fire. The
  // finding vanishes and the run reports `completed`.
  //
  // That hole sits exactly where P4 could open one: switching critics to a tools-restricted
  // agentType is the change most likely to make a critic stage fail, and the harness would have
  // hidden it. Wrap the critic call in this instead of a bare .catch so the loss is counted.
  //   parallel(findings.map(f => () => run.attempt('Verify', agent(...).then(v => ({...f, verdict: v})))))
  run.attempted = 0
  run.lost = 0
  run.attempt = function (stage, promise) {
    run.attempted += 1
    return Promise.resolve(promise).then(
      v => {
        if (v === null || v === undefined) {
          run.lost += 1
          run.signal('critic_starved', stage + ': a critic returned null — the finding it was '
            + 'checking is dropped from the results, NOT cleared. Check the agentType resolves and '
            + 'that a tools-restricted critic can still emit structured output.')
        }
        return v
      },
      err => {
        run.lost += 1
        run.signal('critic_starved', stage + ': a critic threw (' + String(err && err.message || err)
          + ') — the finding it was checking is dropped from the results, NOT cleared.')
        return null
      })
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

  // IDEMPOTENT, AND A COPY. Both properties were missing and both bit immediately.
  //  · summary() SIGNALS on unadjudicated disputes, and wf_attribute_coherence.js calls it twice —
  //    once to hand the run to the guardrail stage, once to return it. Every open dispute was
  //    therefore reported twice, and the guardrail was judging a run whose signal list the final
  //    return then contradicted. The `_summarised` latch fires the signal once, on the first call.
  //  · it returned the LIVE arrays. A caller holding an earlier summary saw it mutate underneath
  //    them, which is the opposite of a snapshot. Now copied.
  // Neither is cosmetic: a report-only harness whose report changes after you read it is worse
  // than no report, because it reads as authoritative.
  run.summary = function () {
    const unadj = run.disagreements.filter(d => d.status === 'open')
    if (unadj.length && !run._summarised) {
      run.signal('disagreement_unadjudicated', unadj.length + ' dispute(s) reached the return with no '
        + 'ruling: ' + unadj.map(d => d.finding_id).join(', '))
    }
    run._summarised = true
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
      signals: run.signals.map(s => Object.assign({}, s)),
      disagreements: run.disagreements.map(d => Object.assign({}, d)),
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

// P8b · build a dispute record FROM a critic verdict, instead of by hand.
//
// WHY THIS EXISTS, and it is not a convenience. Five wave scripts hand-rolled the record as
// `{ layer, target, detail, severity }`. Not one of those four keys is a key run.dispute() reads,
// so every field silently took its default: finding_id became '?', layer_disputed 'interpretation',
// root_cause 'ambiguous-spec', positions []. The record carried ZERO information from its call
// site, and because run.adjudicate() binds on finding_id, no ruling could ever attach to one. That
// shipped and ran live (the W4 run: 8 disputes, all keyed '?'). The three critique scripts wrote it
// correctly, so this was a copy-paste lineage defect — wave0 got it wrong and waves 1-4 inherited.
//
// A record that is error-prone to build by hand gets built by the owner. The correct call is now
// the SHORT one. Hand-rolled records stay legal (the critique scripts have richer positions), so
// the guard that fails on recurrence is static and lives in tools/ci_wf_harness_check.py: it
// derives the legal key set from THIS FILE and rejects a literal run.dispute({...}) that uses a
// key the owner never reads, or that omits finding_id.
//
// The verdict enum below is the uphold/overturn/soften/sharpen funnel every critic stage in this
// repo already emits; the two maps are lifted verbatim from wf_attribute_coherence.js, which had
// them right. `uphold` is not a dispute and callers are expected to filter it out; if one arrives
// anyway it maps to the same conservative defaults as an unrecognised verdict.
const H_LAYER_BY_VERDICT = { overturn: 'evidence', soften: 'severity', sharpen: 'severity' }
const H_ROOT_BY_VERDICT = {
  overturn: 'measurement-vs-assertion',
  soften: 'severity-calibration',
  sharpen: 'severity-calibration',
}
function hVerdictDispute(v, criticLabel, producerHolds) {
  const verdict = v && v.verdict
  return {
    finding_id: String((v && (v.target || v.target_id)) || ''),
    layer_disputed: H_LAYER_BY_VERDICT[verdict] || 'interpretation',
    root_cause: H_ROOT_BY_VERDICT[verdict] || 'ambiguous-spec',
    positions: [
      { by: 'producer', holds: String(producerHolds || '').slice(0, 400) },
      {
        by: String(criticLabel || 'critic'),
        holds: String((v && v.evidence) || '').slice(0, 400),
        verdict: String(verdict || ''),
        severity: String((v && v.severity) || ''),
      },
    ],
    resolution_model: 'adjudicated-by-synthesis',
  }
}

// P4 · the read-only critic. Independence is STRUCTURAL, not a sentence in a prompt: the
// agentType below is defined in .claude/agents/valoria-critic.md with a tools list that has no
// Write/Edit. Passing it is the whole mechanism — a critic stage that omits it can write, and
// tools/ci_wf_harness_check.py fails the script that does.
const H_CRITIC = { agentType: 'valoria-critic' }
function hCritic(opts) { return Object.assign({}, opts || {}, H_CRITIC) }
// ==== END VALORIA WF HARNESS v1 ====
const run = hRun('return-to-game')

const STEP = String(args || '').trim()
if (!STEP) return { error: 'pass the step id as args, e.g. Workflow({scriptPath, args: "S1"})' }

const QUEUE = 'workplans/return_to_game_queue.yaml'

// ── schemas ──────────────────────────────────────────────────────────────────────────────────
const ORIENT_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['step_id', 'precondition_holds', 'evidence', 'actions', 'gate'],
  properties: {
    step_id: { type: 'string' },
    precondition_holds: { type: 'boolean' },
    evidence: { type: 'string', description: 'what you READ on disk to decide that — file:line, not the queue s own done marker' },
    actions: { type: 'array', items: { type: 'string' } },
    gate: { type: 'string', description: 'the exact command or predicate that proves this step finished' },
    blockers: { type: 'array', items: { type: 'string' } },
  },
}

const PRODUCE_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['claims', 'gate_output', 'gate_passed', 'files_changed'],
  properties: {
    claims: {
      type: 'array',
      description: 'one entry per thing you assert you did. A critic will try to break each.',
      items: {
        type: 'object', additionalProperties: false,
        required: ['id', 'claim', 'citation'],
        properties: {
          id: { type: 'string' },
          claim: { type: 'string' },
          citation: { type: 'string', description: 'file:line that substantiates it' },
        },
      },
    },
    gate_output: { type: 'string', description: 'verbatim tail of the gate command output. Never paraphrase it.' },
    gate_passed: { type: 'boolean' },
    files_changed: { type: 'array', items: { type: 'string' } },
    residuals: { type: 'array', items: { type: 'string' }, description: 'anything NOT mechanically attributable. Parked, never guessed.' },
  },
}

const CRITIC_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['lens', 'verdicts'],
  properties: {
    lens: { type: 'string' },
    verdicts: {
      type: 'array',
      items: {
        type: 'object', additionalProperties: false,
        required: ['target', 'verdict', 'why'],
        properties: {
          target: { type: 'string', description: 'the claim id' },
          verdict: { type: 'string', enum: ['uphold', 'overturn', 'soften', 'sharpen'] },
          why: { type: 'string' },
          citation: { type: 'string' },
        },
      },
    },
    missed: { type: 'array', items: { type: 'string' }, description: 'defects the producer did not claim and you found anyway' },
  },
}

const RECONCILE_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['step_state', 'rationale', 'queue_patch'],
  properties: {
    step_state: { type: 'string', enum: ['done', 'blocked', 'pending'] },
    rationale: { type: 'string' },
    queue_patch: { type: 'string', description: 'the exact YAML to write back into the step: evidence, critic_verdict, state' },
    new_queue_entries: { type: 'array', items: { type: 'string' }, description: 'residuals that became their own blocked steps' },
    commit_message: { type: 'string' },
  },
}

const COMMON = `Repo /home/user/ttrpg (Valoria: the DESIGN source of truth for a Godot 4.6 videogame
with NO GM - the engine resolves everything). The implementation repo is jordanelias/valoria-game,
clone it to /workspace/valoria-game if a step needs it.

You are executing ONE step of ${QUEUE}. READ THAT FILE FIRST - its top block is the protocol, and
it carries the measured baselines, the gate tier, the pre-commit checklist and the failure decoder.
Everything you need to avoid a silent stall is in it.

NON-NEGOTIABLE, from CLAUDE.md:
- Never re-implement a rule that already lives once (S8). Compose on the existing primitive.
- A number without a control is not a measurement, in either direction (S0.1 point 4).
- Name the falsifier, or you have not attacked the result (S0.1 point 3).
- Report outcomes faithfully. If a check failed or a step was skipped, say so. A green claim you
  did not verify is worse than a red one you did.
- This repo does not self-schedule (S11). Never arm a wake-up by any mechanism.`

// ── Orient ───────────────────────────────────────────────────────────────────────────────────
phase('Orient')

const orient = await run.attempt('orient', agent(
  `${COMMON}

Load step ${STEP} from ${QUEUE}.

VERIFY ITS PRECONDITION YOURSELF, on disk. Do NOT trust a state: done marker you did not write -
that is the single assumption most likely to make this run produce garbage. If the precondition
names an earlier step, check that step's OBSERVABLE against the tree, not its recorded state.

Return the step's actions and the exact gate predicate. If the precondition does not hold, say so
and list what is missing. Do not start the work.`,
  { label: `orient:${STEP}`, phase: 'Orient', model: 'sonnet', effort: 'medium', schema: ORIENT_SCHEMA }))

if (!orient) { run.signal('null_result', 'orient returned nothing'); return { step: STEP, summary: run.summary(), error: 'orient failed' } }
if (!orient.precondition_holds) {
  log(`${STEP}: precondition does NOT hold - ${(orient.blockers || []).join('; ')}`)
  return { step: STEP, state: 'pending', reason: 'precondition unmet', blockers: orient.blockers, summary: run.summary() }
}

// ── Produce ──────────────────────────────────────────────────────────────────────────────────
phase('Produce')

const produced = await run.attempt('produce', agent(
  `${COMMON}

EXECUTE step ${STEP}. Its actions, as loaded:
${(orient.actions || []).map((a, i) => `${i + 1}. ${a}`).join('\n')}

Its gate: ${orient.gate}

RULES OF EXECUTION:
- Do exactly these actions. Do not widen the step. If you find adjacent work, record it as a
  residual - the queue has a place for it - and leave it.
- Run the gate and capture its output VERBATIM. Where the gate is a fixed-point iteration, iterate;
  PASS is a fixed point with an empty delta, NEVER a low count. Godot reports only the first parse
  error per file, so fixing a layer uncovers the next and the count can RISE mid-iteration.
- Follow the pre_commit_checklist in the queue file for whatever change class you touched. A
  prose-only commit stales three generated artifacts and costs ~800 lines of regeneration churn.
- Consult failure_decoder in the queue file BEFORE diagnosing any red. Several gates that look
  blocking are report-only, and one that looks report-only (review_core) is blocking-on-regression.
- Do NOT commit. The caller commits after the critics rule.

Return one CLAIM per thing you assert you did, each with a file:line citation. Three independent
critics will try to break each claim and they will only see your claims and artifacts - never this
prompt and never your reasoning. A claim you cannot cite is one you should not make.`,
  { label: `produce:${STEP}`, phase: 'Produce', model: 'sonnet', effort: 'high', isolation: 'worktree', schema: PRODUCE_SCHEMA }))

if (!produced) { run.signal('null_result', 'produce returned nothing'); return { step: STEP, summary: run.summary(), error: 'produce failed' } }

// ── Critique — three lenses, structurally read-only ──────────────────────────────────────────
// hCritic() routes to .claude/agents/valoria-critic.md (tools: Read, Grep, Glob). The critics
// receive the producer's OUTPUT and never its reasoning: that is what makes this a relay rather
// than a dialogue, and it is why the independence is structural rather than promised in a prompt.
phase('Critique')

const ARTIFACTS = `STEP: ${STEP}
FILES CHANGED: ${(produced.files_changed || []).join(', ') || '(none reported)'}
GATE PASSED (as claimed): ${produced.gate_passed}
GATE OUTPUT (verbatim, as captured by the producer):
${produced.gate_output}

CLAIMS:
${(produced.claims || []).map(c => `[${c.id}] ${c.claim}\n      citation: ${c.citation}`).join('\n')}

RESIDUALS THE PRODUCER PARKED:
${(produced.residuals || []).join('\n') || '(none)'}`

const LENSES = [
  {
    key: 'fidelity',
    prompt: `LENS: FIDELITY - does the change do what it claims, and ONLY that?
Read the actual diff on disk. For each claim: does the code change match the claim's description?
Did the producer widen the step beyond its stated actions? Did it special-case an entity or an
outcome (scripting drift) rather than fixing the general rule? Did it re-implement something that
already lives once elsewhere in the tree? Overturn any claim whose diff does something other than,
or more than, what it says.`,
  },
  {
    key: 'factuality',
    prompt: `LENS: FACTUALITY - does every citation say what it is claimed to say?
Open every cited file at every cited line and read it. A claim whose citation does not substantiate
it is OVERTURNED, not softened - the anti-fabrication gate in this repo is leaky by design limit
(CLAUDE.md S7), so hand verification IS the check. Also re-derive the gate verdict yourself from the
gate output rather than trusting the producer's gate_passed boolean: re-grep it, recount it. If the
gate was a fixed-point iteration, check that the final iteration applied zero fixes.`,
  },
  {
    key: 'logic',
    prompt: `LENS: LOGIC - does the conclusion follow, and would the gate have caught the failure?
For each claim, ask what would have to be true for it to be wrong, and whether the gate could
observe that. A gate that cannot observe the failure it excludes is an ABSENT test, not a weak one.
Look for confounds: is the "before" and the "after" the same experiment? Is a favourable result
uncontrolled? Did a read/write asymmetry make some writer silently a no-op? Overturn any claim
whose supporting measurement cannot distinguish success from failure.`,
  },
]

const cFirst = await agent(`${COMMON}\n\n${ARTIFACTS}\n\n${LENSES[0].prompt}`,
  hCritic({ label: `critic:${LENSES[0].key}`, phase: 'Critique', model: 'opus', effort: 'high', schema: CRITIC_SCHEMA }))

const cRest = await parallel(LENSES.slice(1).map(l => () =>
  agent(`${COMMON}\n\n${ARTIFACTS}\n\n${l.prompt}`,
    hCritic({ label: `critic:${l.key}`, phase: 'Critique', model: 'opus', effort: 'high', schema: CRITIC_SCHEMA }))))

const critics = [cFirst].concat(cRest).filter(Boolean)
for (const c of critics) run.lens(c.lens || 'unknown', c.verdicts || [])
run.critiqued('produce', (produced.claims || []).length, critics.reduce((n, c) => n + (c.verdicts || []).length, 0))

// P7b · rank the critic-found defects by INDEPENDENT REDISCOVERY. Three lenses attack the same
// artifacts from different angles, so a defect two or three of them surface separately is far more
// bankable than one a single lens raised — and the alarm on a lens that returned nothing must never
// become pressure to manufacture findings, which is why the ranking ships paired with it.
const missedFindings = critics.flatMap(c =>
  (c.missed || []).map(m => ({ claim: String(m), evidence: String(m), _lens: c.lens })))
const rankedMissed = hRediscover(missedFindings, f => f._lens)

const allVerdicts = critics.flatMap(c => (c.verdicts || []).map(v => Object.assign({}, v, { _lens: c.lens })))
const overturned = allVerdicts.filter(v => v.verdict === 'overturn')
for (const v of overturned) {
  run.dispute(hVerdictDispute(v, v._lens, 'producer asserted the claim with a citation'))
}

// ── Reconcile ────────────────────────────────────────────────────────────────────────────────
phase('Reconcile')

const reconciled = await run.attempt('reconcile', agent(
  `${COMMON}

Step ${STEP} was produced, then attacked by three independent read-only critics on distinct lenses.

${ARTIFACTS}

CRITIC VERDICTS:
${allVerdicts.map(v => `[${v._lens}] ${v.target}: ${v.verdict} - ${v.why}${v.citation ? ' (' + v.citation + ')' : ''}`).join('\n') || '(none returned)'}

DEFECTS CRITICS FOUND THAT THE PRODUCER DID NOT CLAIM, ranked by how many lenses independently
surfaced each one (a defect two or three lenses found separately is the bankable kind):
${rankedMissed.map(g => `[x${g.rediscovery} - ${(g.lenses || []).join(',')}] ${g.findings[0].claim}`).join('\n') || '(none)'}

ADJUDICATE. Rules:
- ANY overturn on a load-bearing claim means step_state is NOT done. Either the producer must redo
  it, or the step is blocked with the reason recorded. Do not average verdicts into a pass.
- A soften or a sharpen adjusts the recorded evidence; it does not block.
- A critic returning zero verdicts is a NULL RESULT, not a clean bill of health. Say so.
- Residuals and critic-found defects that are real but out of this step's scope become NEW queue
  entries with state: blocked and a file:line - parked, never guessed, never silently fixed.

Return the exact YAML to write back into step ${STEP} (evidence, critic_verdict, state) and a
commit message in the repo's [scope] description format citing ${STEP}.`,
  { label: `reconcile:${STEP}`, phase: 'Reconcile', model: 'opus', effort: 'high', schema: RECONCILE_SCHEMA }))

if (!reconciled) { run.signal('null_result', 'reconcile returned nothing') }

for (const v of overturned) {
  run.adjudicate(String(v.target || ''), `reconcile applied the overturn from the ${v._lens} lens`, 'reconcile')
}
for (const d of run.disagreements) {
  if (d.status === 'open') run.adjudicate(d.finding_id, 'no counter-evidence was produced; carried at the critic-assigned severity', 'reconcile')
}

return {
  step: STEP,
  summary: run.summary(),
  state: reconciled ? reconciled.step_state : 'blocked',
  rationale: reconciled ? reconciled.rationale : 'reconcile stage returned nothing',
  queue_patch: reconciled ? reconciled.queue_patch : null,
  commit_message: reconciled ? reconciled.commit_message : null,
  new_queue_entries: reconciled ? (reconciled.new_queue_entries || []) : [],
  claims: (produced.claims || []).length,
  verdicts: allVerdicts.length,
  overturned: overturned.length,
  missed_ranked: rankedMissed.slice(0, 10).map(g => ({ n: g.rediscovery, lenses: g.lenses, claim: g.findings[0].claim })),
  critic_lenses_returning_nothing: LENSES.map(l => l.key).filter(k => !critics.some(c => c.lens === k)),
}
