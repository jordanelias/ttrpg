export const meta = {
  name: 'world-schema-gaps',
  description: 'World-schema gap audit (ED-IN-0153): interrogate the entity ladder (character -> settlement -> settlement faction/governance -> territory/province -> provincial faction/governance -> national faction/governance) and 18 domain lenses against the Key type registry + module contracts, to find MISSING keys and contracts. Read-only: produces a gap register, ratifies nothing.',
  phases: [
    { title: 'Strata', detail: '4 ladder-first lanes: character-binding, settlement+subnational, territory/province+provincial, national+cross-scale', model: 'sonnet' },
    { title: 'Lenses', detail: '5 lens-first lanes over the same ladder: interior life, social order, material/martial, governance/relations, dynamics', model: 'sonnet' },
    { title: 'Config', detail: '3 individuation lanes: what a character / a faction at each tier / a settlement and world need AUTHORED to be unique and narratively consequential', model: 'sonnet' },
    { title: 'Adversarial', detail: 'read-only valoria-critic relay over the merged findings, 4 disjoint clusters', model: 'opus' },
    { title: 'Synthesis', detail: 'dedup, rediscovery ranking, dispute adjudication, gap register', model: 'opus' },
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
// ---------------------------------------------------------------------------------------------
// METHOD (CLAUDE.md sections 0 and 10). Two fan-outs decompose the SAME subject along orthogonal
// axes, so a gap hit by both is corroborated by method-disjoint rediscovery rather than by one
// lane arguing harder. This is the ED-IN-0152 second-pass pattern applied prospectively instead
// of retrospectively.
//   Pass A (Strata) walks the entity ladder and asks, per rung: what does canon say this rung IS,
//     and which of those facts has no key type and no contract expression?
//   Pass B (Lenses) walks 18 domain lenses and asks the same question across every rung at once.
//   A finding both passes reach independently ranks above one only a single lane reached.
//
// GROUNDING (measured this session, so lanes start from fact and spend their budget on the gap,
// not on rediscovering the inventory):
//   - 55 key types in systems/_architecture/key_type_registry_v30.md, families scene./da./
//     mechanical./state./env./meta.  27 modules in references/module_contracts.yaml (26 extracted,
//     1 stub).  Generated views: references/KEY_INDEX.md, references/CONTRACT_INDEX.md,
//     references/ENGINE_ATLAS.md.
//   - The contract scales enum is 7-valued [personal, scene, settlement, territory, provincial,
//     peninsula, thread] and is [ASSUMPTION]-grade. There is NO national scale; 'peninsula' is the
//     top. Four scale vocabularies are unreconciled and HELD at ED-IN-0103 fork 1 - lanes RECORD
//     that seam, they do not resolve it.
//   - scale_hierarchy_v1.md (Jordan-ratified 2026-07-13, B12) rules the ladder Country > Duchy >
//     Province > Territory > Settlement. Code has one intermediate dataclass, Territory in
//     engine/autoload/game_state.py, which is the OLD PP-726 'Province'. No Duchy, no Province,
//     no B12 Territory tier exists in code or in any contract.
//   - No Character/PlayerCharacter class exists anywhere; identity is a bare actor_id string.
//     There is no settlement_id on any character or NPC.
//   - key_type_registry section 10 forbids appending a new key type without a row in
//     references/rendering_dispositions.yaml, WHICH DOES NOT EXIST. So this audit proposes; it
//     cannot legally append. That is a finding in its own right, not an obstacle to route around.
//
// SCOPE STOP. This run edits NOTHING. No lane may propose a rename of an existing key type or
// contract module (the dotted-namespace question is HELD for Jordan, ED-IN-0152). Findings are
// observations against the tree; dispositioning them is per-lane design work.
// ---------------------------------------------------------------------------------------------

const run = hRun('world-schema-gaps')

const GAP_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['lane', 'coverage', 'surfaces_read', 'clean', 'findings'],
  properties: {
    lane: { type: 'string' },
    coverage: { type: 'string', description: 'What you actually read and what you did NOT reach. A reader uses this to tell a clean surface from an unread one.' },
    surfaces_read: { type: 'array', items: { type: 'string' } },
    clean: { type: 'array', items: { type: 'string' }, description: 'Things you checked that are genuinely PRESENT and adequately keyed/contracted. Absence of findings must be distinguishable from absence of looking.' },
    findings: {
      type: 'array',
      items: {
        type: 'object', additionalProperties: false,
        required: ['claim', 'gap_kind', 'rung', 'lens', 'proposal', 'evidence', 'existing_tracking', 'confidence'],
        properties: {
          claim: { type: 'string', description: 'One sentence: what the world model requires that the schema does not express.' },
          gap_kind: { enum: ['missing_key_type', 'missing_contract_module', 'missing_owned_state', 'missing_edge', 'missing_scale_or_transition', 'missing_payload_field', 'missing_authoring_schema', 'missing_individuation_descriptor', 'vocabulary_conflict', 'declared_but_unimplemented'] },
          rung: { type: 'string', description: 'character | settlement | settlement_faction | territory | province | provincial_faction | national_faction | national_governance | cross_rung' },
          lens: { type: 'string' },
          proposal: { type: 'string', description: 'The concrete addition: a key type_id with required_payload_fields, or the exact module_contracts.yaml field/row. Compose on an existing primitive; never special-case an entity.' },
          evidence: { type: 'string', description: 'file:line citations. A claim whose citation does not say what the claim says is overturned, not softened.' },
          existing_tracking: { type: 'string', description: 'The ED-<LANE>-NNNN / PP-NNN / gap_note that already tracks this, or "none found" after actually grepping the ledgers.' },
          confidence: { enum: ['high', 'medium', 'low'] },
        },
      },
    },
  },
}

const CRITIC_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['verdicts', 'missed', 'coverage'],
  properties: {
    coverage: { type: 'string' },
    verdicts: {
      type: 'array',
      items: {
        type: 'object', additionalProperties: false,
        required: ['target', 'verdict', 'severity', 'evidence'],
        properties: {
          target: { type: 'string', description: 'The claim text you are ruling on, verbatim enough to bind.' },
          verdict: { enum: ['uphold', 'overturn', 'soften', 'sharpen'] },
          severity: { enum: ['high', 'medium', 'low'] },
          evidence: { type: 'string' },
        },
      },
    },
    missed: { type: 'array', items: { type: 'string' }, description: 'Gaps the producers did not reach, found by reading at least one surface they did not cite.' },
  },
}

const SYNTH_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['register', 'ladder_verdict', 'held_for_jordan', 'residuals'],
  properties: {
    ladder_verdict: { type: 'string' },
    register: {
      type: 'array',
      items: {
        type: 'object', additionalProperties: false,
        required: ['id', 'claim', 'gap_kind', 'rung', 'lenses', 'proposal', 'evidence', 'rediscovery', 'existing_tracking', 'disposition'],
        properties: {
          id: { type: 'string', description: 'G-01, G-02, ... ranked most-corroborated first.' },
          claim: { type: 'string' },
          gap_kind: { type: 'string' },
          rung: { type: 'string' },
          lenses: { type: 'array', items: { type: 'string' } },
          proposal: { type: 'string' },
          evidence: { type: 'string' },
          rediscovery: { type: 'number', description: 'How many INDEPENDENT lanes reached it. Strata and lens lanes are method-disjoint, so a cross-pass hit is worth more than two same-pass hits.' },
          existing_tracking: { type: 'string' },
          disposition: { enum: ['propose_key', 'propose_contract', 'propose_descriptor', 'propose_authoring_field', 'already_tracked', 'needs_jordan_ruling', 'not_a_gap'] },
        },
      },
    },
    held_for_jordan: { type: 'array', items: { type: 'string' } },
    residuals: { type: 'array', items: { type: 'string' }, description: 'What this run did NOT cover, stated plainly.' },
  },
}

const COMMON = `Repo /home/user/ttrpg (Valoria: a Godot videogame with NO GM - the engine resolves
everything). Read CLAUDE.md sections 0 and 0.1 first. You are READ-ONLY in practice: your return
value is the deliverable; do not edit any file.

THE QUESTION. Not "is this system built?" - that is already measured and is not what we are after.
The question is: **what does the world model logically require that the SCHEMA cannot express?**
The schema is exactly two authored surfaces:
  - systems/_architecture/key_type_registry_v30.md  (55 key types; format at its section 1:
    type_id, description, required_payload_fields, optional_payload_fields, default_scale_signature,
    default_permanence, default_time_horizon, emitting_systems, consuming_systems)
  - references/module_contracts.yaml  (27 modules; fields module, doc, sim_module, scales, resolver,
    consumes[{type,from}], emits[{type,terminal}], state[{name,bucket,writable}], transitions,
    loops, gates, derivations, accounting_phase, gap_notes, status, sources)
Read the GENERATED views first, they are cheap and current: references/KEY_INDEX.md (per-key
producers/consumers + a review queue of terminating chains and under-declarations),
references/CONTRACT_INDEX.md (per-module IN/resolver/OUT + A1-A12 violations),
references/ENGINE_ATLAS.md (declared vs executed). Then read the AUTHORED sources for anything you
intend to claim about - the views are joins and can mislead about intent.

WHAT COUNTS AS A FINDING. A fact the design canon asserts about the world, which no key type can
carry and no contract row can hold. Examples of the SHAPE (not a list to fill):
  - a relation that exists in prose and has no state field to live in on either side;
  - a state change the world can undergo that emits nothing, so no other system can ever learn of it;
  - an entity every rung above and below references, that owns no contract and no scale value;
  - a payload that cannot express the arity canon requires (one-to-one where canon says many-to-many);
  - a key whose default_scale_signature has no value for the scale the canon event happens at.
A module that is merely UNBUILT is NOT a finding here - "declared_but_unimplemented" is a gap_kind
only when the declaration itself is incoherent or the absence hides a missing schema element.

DISCIPLINE, and these are the failure modes this corpus actually has:
  1. Pattern-matching on a term instead of the concept is the single error that has cost this
     project the most rework. Before claiming X is missing, grep the ADJACENT subsystem where this
     corpus tends to actually keep it.
  2. Every claim carries file:line. A claim you cannot cite is not a finding.
  3. Grep registers/editorial_ledger*.jsonl and the module's own gap_notes before filing anything -
     31 open ledger items already touch keys/contracts/schema. Report the ED id in
     existing_tracking; "none found" is a claim you must have actually tested.
  4. Compose on the existing primitive. Never propose special-casing a named entity (scripting
     drift) or a scale-local dialect (shape divergence).
  5. Finding nothing is a real verdict. Populate 'clean' so a reader can tell a clean surface from
     an unread one; do not manufacture findings.
NO RENAMES: the dotted-namespace proposal is HELD for Jordan (ED-IN-0152). NO scale-vocabulary
unification: HELD at ED-IN-0103 fork 1. Record those seams where you hit them; do not resolve them.`

const LADDER = `THE ENTITY LADDER, as ratified and as built (measured this session - these are
LEADS, re-verify at the cited path):
  character -> settlement -> settlement faction + settlement governance -> territory/province ->
  provincial faction + provincial governance -> national faction + national governance.
  - systems/settlements/scale_hierarchy_v1.md is Jordan-ratified (2026-07-13, B12): Country >
    Duchy > Province (conditional) > Territory (NEW tier) > Settlement. Its own section 6 says the
    mechanical rewrite is NOT executed.
  - engine/autoload/game_state.py has Faction (4 static instances) and Territory (T1-T17, which is
    the OLD PP-726 'Province'). systems/settlements/sim/registry.py has Settlement (37, each with
    province_id pointing at a T-code). There is no Duchy, no Province, no B12 Territory, and no
    Character class anywhere.
  - references/module_contracts.yaml scales enum: [personal, scene, settlement, territory,
    provincial, peninsula, thread]. No 'national'.`

// ---------------------------------------------------------------------------------------------
// PASS A - STRATA. Cache discipline (ED-IN-0087 fact 1): concurrent agents sharing a prefix all
// pay full price because an entry is readable only once the first response begins streaming. So
// the first lane is fired and AWAITED, and the remaining three fan out behind its warm cache.
// ---------------------------------------------------------------------------------------------
phase('Strata')

const A_LANES = [
  {
    key: 'A1-character-binding',
    prompt: `Lane A1 - THE CHARACTER RUNG AND EVERY BINDING OUT OF IT.
Subject: what a character IS to the schema, and how a character binds to a settlement, to a
faction at any tier, to an office, to a territory, and to another character.
Start from: systems/characters/ (all docs + sim/), systems/characters/characters_flow_skeleton_v1.md,
systems/npcs/npc_behavior_v30.md, systems/world/sim/npe.py (NPC dataclass), the piety_track and
npc_behavior and npc_memory rows in references/module_contracts.yaml,
systems/_architecture/player_agency_v30.md (Scene Slate, Standing/Duty/Conviction).
Specific things to interrogate - each is a lead, not a conclusion:
  - identity is a bare actor_id string with no owning class or contract. What schema elements does
    that absence make unexpressible?
  - NPC.territory_id binds to the province grain and NPC.affiliation_faction to one of 4 flat
    national factions. Settlement.npc_ids exists on the Settlement dataclass. Is there any key or
    contract state that expresses membership, office-holding, or residence?
  - can a character belong to more than one faction, hold an office at one tier while resident at
    another, or change affiliation? What key would carry that transition? Is there one?
  - state.scar_acquired / state.belief_revised / state.opinion_revised are declared. What character
    state changes have NO key at all?`,
  },
  {
    key: 'A2-settlement-and-subnational',
    prompt: `Lane A2 - SETTLEMENT, SETTLEMENT FACTION, SETTLEMENT GOVERNANCE.
Start from: systems/settlements/settlement_layer_v30.md (esp. sections 3.1-3.3 the Two-Tier
Authority Model and Subnational Faction Governance, and 6.1-6.3 the Stature Ladder / faction
emergence), systems/settlements/governance_play_redesign_v1.md, settlement_adjacency_v30.md,
territory_temperaments_v30.md, systems/settlements/sim/registry.py, the settlements flow skeleton,
and the settlement_layer + settlement_economy rows in references/module_contracts.yaml.
Interrogate:
  - section 3.3 names 7 subnational-faction archetypes that can govern a settlement. In code that
    is Settlement.subnational: dict (foothold -> level). Is there ANY contract module, owned-state
    row, or key type for a settlement-scale faction? If not, what is the minimal schema that would
    express one without special-casing the 7 archetypes?
  - Settlement.legitimacy and .popular_support are declared 0-7 and never read or written. Is the
    gap a missing key (nothing can change them) or a missing contract row (nobody owns them)?
  - governor succession: succeed_governor has zero production callers, and state.succession is
    declared with a territory/peninsula scale signature. Can a settlement-scale succession even be
    expressed by the existing key?
  - the Stature Ladder / Renown-driven emergence of a NEW faction from a settlement: what key type
    announces a faction coming into existence? Does one exist for ANY tier?
  - two uncoordinated stores: World.territories (T1-T17) and World.settlements (37, province_id ->
    T-code), with a report-only drift probe in systems/overview/sim/accounting.py. Is the
    settlement->province binding declared anywhere in the schema, or only in code?`,
  },
  {
    key: 'A3-territory-province-provincial',
    prompt: `Lane A3 - TERRITORY / PROVINCE, AND PROVINCIAL FACTIONS + GOVERNANCE.
This is the rung where the ratified design and the schema diverge most, so be precise about which
of the two 'Territory's you mean in every claim.
Start from: systems/settlements/scale_hierarchy_v1.md (RATIFIED B12 ladder, section 5.1 rules
faction tiers local/provincial/national INDEPENDENT and not containment-nested; section 6 lists the
unexecuted rewrite), systems/factions/fractional_province_ownership_v30.md (PP-666, pre-B12),
systems/factions/franchise_v30.md (DRAFT, per-territory Franchise 0-5 feeding national Influence),
systems/world/geography_v30.md, systems/settlements/valoria_geography_v30.yaml,
engine/autoload/game_state.py Territory dataclass, and every module in module_contracts.yaml whose
scales include territory or provincial.
Interrogate:
  - the B12 Territory tier exists in ratified design and in NO contract, NO key scale value, and NO
    code. What schema elements does the whole ladder need to carry it? Is 'territory' in the
    contracts scales enum the B12 tier or the old province - and can any reader of the schema tell?
  - Province is CONDITIONAL in B12 (it exists only while its territories share a faction). No key
    type announces a province forming or dissolving. Is that expressible at all?
  - fractional province ownership and Franchise: what owned state and what key would these need?
    Which module would own them - does that module exist?
  - provincial-tier factions have no class, no contract, no key. Given section 5.1 rules the tiers
    independent, is a single 'faction' contract even schema-adequate, or does the tier need to be a
    field on faction state? Propose the minimal composable form, not a new module per tier.
  - Territory.accord is written directly at systems/factions/sim/parliamentary_transfer.py and
    mass_seizure.py, bypassing Settlement.order. Is there a missing aggregate/distribute
    declaration (see systems/_architecture/propagation_spec_v1.md)?`,
  },
  {
    key: 'A4-national-and-cross-scale',
    prompt: `Lane A4 - NATIONAL FACTIONS, NATIONAL GOVERNANCE, AND THE CROSS-SCALE SPINE.
Start from: systems/factions/faction_canon_v30.md, faction_layer_v30.md, faction_behavior_v30.md,
faction_state_authoring_v30.md, faction_politics_v30.md (Standing 0-7 ladder, sub-office ladders,
caste, coup, succession), baralta_crown_claim_v30.md, parliamentary_transfer_v30.md,
ci_political_v30.md; the faction_state / faction_politics / ci_political / domain_actions rows in
module_contracts.yaml; engine/cross_scale/ (all modules); and
systems/_architecture/scale_transitions_v30.md + propagation_spec_v1.md.
Interrogate:
  - there is no 'national' value in the contracts scales enum; 'provincial' and 'peninsula' are
    used for what canon calls national. Is that a vocabulary conflict to RECORD (held at ED-IN-0103
    fork 1) or a genuinely missing scale value? Say which, with evidence, and do not resolve it.
  - faction_politics declares Standing / Coup posture / Succession status as owned state with
    sim_module: none, and state.coup_attempted / state.succession / state.standing_change as keys.
    Is the SCHEMA adequate for the design (rank ladders, sub-offices, caste), or does the design
    require payload/state the registry cannot carry?
  - engine/cross_scale/ bridges exactly personal/scene <-> faction. module_contracts.yaml names the
    transition 'scale_transitions section 3.2 Personal -> Faction', skipping settlement and
    territory by name. CONTRACT_INDEX reports 20 A6 violations (cross-scale edges with no
    transitions entry) across 9 module pairs. Which of those 9 are a MISSING TRANSITION DECLARATION
    versus a missing key? Be specific per pair.
  - Domain Echo: classify_scene_outcome requires an echo['scene_outcome'] field no live producer
    sets. Is that a missing required_payload_field on a key type? Name it.
  - what announces a faction being created, destroyed, merged, or split? Any tier.`,
  },
]

const aFirst = await agent(COMMON + '\n\n' + LADDER + '\n\n' + A_LANES[0].prompt,
  { label: A_LANES[0].key, phase: 'Strata', model: 'sonnet', effort: 'high', schema: GAP_SCHEMA })

const aRest = await parallel(A_LANES.slice(1).map(l => () =>
  agent(COMMON + '\n\n' + LADDER + '\n\n' + l.prompt,
    { label: l.key, phase: 'Strata', model: 'sonnet', effort: 'high', schema: GAP_SCHEMA })))

const strata = [aFirst].concat(aRest).filter(Boolean)
for (const r of strata) run.lens('strata:' + r.lane, r.findings)
run.round('strata', strata.flatMap(r => r.findings || []))

// ---------------------------------------------------------------------------------------------
// PASS B - LENSES. Same subject, orthogonal decomposition. These lanes never see Pass A's output:
// the whole value of the second axis is that its rediscoveries are independent.
// ---------------------------------------------------------------------------------------------
phase('Lenses')

const B_LANES = [
  {
    key: 'B1-interior-life',
    lenses: 'personal beliefs and convictions · values and ethics · goals and ambitions · personal history',
    hint: `systems/characters/conviction_taxonomy_v30.md (13 Convictions), conviction_axis_matrix_v30.md,
conviction_track_v1.md, systems/characters/sim/{conviction,beliefs}.py, references/descriptor_registry.yaml
(conviction_weight / ethical_axis / conviction_axis_map KINDs), the npc_memory contract row (state: []
and no store in code), systems/settlements/governance_play_redesign_v1.md section 3.2 'ambition engine'
(PROPOSAL). Ask especially: an AMBITION is a forward-looking commitment - the schema has Mission at
faction scale and nothing at personal scale; what key announces a goal formed, advanced, abandoned,
achieved? And: memory is a declared consumer with no store - what owned state is missing, on which module?`,
  },
  {
    key: 'B2-social-order',
    lenses: 'social status · society (class, caste, culture, custom) · demographics · religion',
    hint: `systems/factions/faction_politics_v30.md (Standing 0-7 ladder, caste system, sub-office ladders),
systems/characters/conviction_track_v30.md (the TERRITORIAL Piety Track - note the documented 3-way
name collision with piety_track/territorial_piety, CONTRACT_INDEX.md:104), systems/factions/ci_political_v30.md,
systems/overview/sim/ci_track.py, the territorial_piety + ci_political + piety_track contract rows.
Ask especially: 'institutional_culture' is a per-faction scalar and there is no class/caste/culture
system at settlement or character scale - is that a missing lens or deliberately folded? Demographics:
env.population_change is a declared key and NO module owns a population stat (settlement_economy's own
gap_note calls Population a deferred DESIGN decision) - is that a missing owned_state row, and on which
module? Religion: mechanical.theocracy_unification_declared is declared with zero emitters.`,
  },
  {
    key: 'B3-material-and-martial',
    lenses: 'economics · military · invasion threats · geography',
    hint: `systems/settlements/settlement_layer_v30.md sections 1.3/1.8 (the real economics), the
settlement_economy contract row (doc: null, gap_note 'RECOMMEND RETIRE ... phantom module'),
systems/mass_battle/ (docs + sim + the 28-module canon tree at tests/sim/mass_battle/ per Jordan
ruling J2), the mass_battle contract row (state: [] - explicitly empty), systems/world/geography_v30.md
+ systems/settlements/sim/adjacency.py, systems/mass_battle/sim/altonian_reinforcements.py (raises
NotImplementedError unconditionally). Ask especially: trade/supply/resource flow BETWEEN settlements or
provinces - does any key or contract state carry it, or is economics purely a per-settlement scalar?
Military: 'Mil' lives inside faction_state's unnamed 'faction stats 1-7' bucket and mass_battle.state is
empty - what owned state does an army/levy/garrison need that no module declares? Invasion: env.crisis
has crisis_type: invasion as one enum value and there is no invasion entity, no external-power actor,
and no key for an incursion beginning or ending. Geography: adjacency, distance and terrain have real
code and NO contract module and NO key scale of their own - what would owning them look like?`,
  },
  {
    key: 'B4-governance-and-relations',
    lenses: 'politics · geopolitics · diplomacy · world history',
    hint: `systems/factions/faction_layer_v30.md section 3 (Treaty Mechanics), treaty_expiration_v30.md,
systems/factions/sim/treaty.py, parliamentary_* docs and sim, baralta_crown_claim_v30.md,
canon/03_canonical_timeline.md, systems/articulation/articulation_layer_v30.md section 4 (Tier 3
Chronicle Generator) and engine/cross_scale/articulation.py (every function is a stub_resolve no-op).
Ask especially: DIPLOMACY has a doc, real code in treaty.py, and da.diplomatic_alliance - but treaties
appear in NO module's state: block. Who owns a treaty? What is its lifecycle and which keys carry it?
GEOPOLITICS returned ZERO hits across every systems/ doc, contract and key - before filing that as
absent, grep the adjacent surfaces where this corpus keeps such things (faction relations, the
peninsular strain tracks, the world churn machinery at ED-IN-0149) and say precisely what exists under
another name and what genuinely does not. WORLD HISTORY: mechanical.era_transition and
mechanical.second_calamity are declared with zero live emitters and no consumers - is the chronicle a
missing consumer declaration or a missing owned state?`,
  },
  {
    key: 'B5-dynamics',
    lenses: 'events · threadwork · the churn seam',
    hint: `systems/overview/peninsular_strain_v30.md + sim (Turmoil/IP/MS tracks), systems/world/
miraculous_event_v30.md + sim, systems/threadwork/threadwork_v30.md + systems/threadwork/sim/operations.py +
thread_horizontal_integration_spec.md, systems/overview/clock_registry_v30.md (self-declared single
source of truth for all clocks/tracks/counters), the clock_registry + engine_clock + game_director +
peninsular_strain contract rows, and audit/2026-08-08-world-churn-audit/ (ED-IN-0149: the churn
machinery is built and DISCONNECTED). Ask especially: EVENTS - env.crisis has 2 producers and NO
consumers; mechanical.season_change and mechanical.settlement_captured and state.settlement_revolt and
mechanical.era_transition and mechanical.second_calamity likewise terminate. Which of those 8
consumerless keys are legitimately terminal world-events and which are a missing consumer contract?
Rule per key, with evidence - this is one of the four decisions HELD for Jordan at ED-IN-0151, so
produce the EVIDENCE for the ruling, do not make the ruling. THREADWORK is one of the few
well-modelled lenses: say what it does that the thin lenses do not, because that is the template the
proposals should follow. And: does threadwork's scale value 'thread' set a precedent for how a
non-spatial scale enters the enum?`,
  },
]

const bFirst = await agent(COMMON + '\n\n' + LADDER + '\n\nLane ' + B_LANES[0].key +
  ' - LENS-FIRST SWEEP.\nYour lenses: ' + B_LANES[0].lenses + `.
Sweep the WHOLE ladder (character, settlement, settlement faction, territory, province, provincial
faction, national faction, national governance) through these lenses only. For each lens ask: what
does this domain require the world to remember, to change, and to announce - and which of those has
no owned-state row and no key type? Set 'rung' on every finding.
Leads: ` + B_LANES[0].hint,
  { label: B_LANES[0].key, phase: 'Lenses', model: 'sonnet', effort: 'high', schema: GAP_SCHEMA })

const bRest = await parallel(B_LANES.slice(1).map(l => () =>
  agent(COMMON + '\n\n' + LADDER + '\n\nLane ' + l.key + ' - LENS-FIRST SWEEP.\nYour lenses: ' +
    l.lenses + `.
Sweep the WHOLE ladder (character, settlement, settlement faction, territory, province, provincial
faction, national faction, national governance) through these lenses only. For each lens ask: what
does this domain require the world to remember, to change, and to announce - and which of those has
no owned-state row and no key type? Set 'rung' on every finding.
Leads: ` + l.hint,
    { label: l.key, phase: 'Lenses', model: 'sonnet', effort: 'high', schema: GAP_SCHEMA })))

const lenses = [bFirst].concat(bRest).filter(Boolean)
for (const r of lenses) run.lens('lens:' + r.lane, r.findings)

// ---------------------------------------------------------------------------------------------
// PASS C - CONFIGURATION / INDIVIDUATION. A third axis, and a different question from A and B.
// A and B ask what the engine must REMEMBER and ANNOUNCE. C asks what must be AUTHORED at setup
// for an entity to be distinguishable from its peers and for that distinction to propagate into
// play. A world of 37 identical settlements and 4 stat-block factions emits keys perfectly well
// and produces no narrative. The schema question is the same shape: which individuating facts
// have no descriptor, no authoring field, and no contract row to live in?
// ---------------------------------------------------------------------------------------------
phase('Config')

const CONFIG_COMMON = `THE INDIVIDUATION QUESTION. Ask, for your subject: what does an instance of
this need AUTHORED - not computed at runtime - so that it is (a) distinguishable from every other
instance, (b) consequential, i.e. that distinction changes what happens rather than only how it
reads, and (c) legible, i.e. some system can act on the distinction. Then ask which of those facts
has no home: no KIND in references/descriptor_registry.yaml, no owned-state row in
references/module_contracts.yaml, no authoring field in the generator or authoring doc, and no key
that can carry it when it changes.

The three failure shapes to look for specifically:
  1. FLAVOUR WITH NO HOOK - the doc gives an instance a distinguishing trait and no system reads it,
     so two instances differ in prose and are identical in play.
  2. HOOK WITH NO VARIATION - a stat every instance carries at the same value, or a template with
     one filled row, so the mechanism exists and individuation does not.
  3. HARDCODED SINGLETON - the distinction is written as a named branch in code rather than as data
     on the instance, so a new instance cannot have it. This is scripting drift and it is the
     failure mode this repo is most exposed to; name every one you find.
Emergence is the goal: individuation should come from composing the SAME small descriptor set
differently per instance, never from a per-entity special case. A proposal that adds a bespoke
field for one named faction or one named settlement is a defect even if the gap is real.`

const C_LANES = [
  {
    key: 'C1-character-individuation',
    prompt: `Lane C1 - WHAT MAKES A CHARACTER UNIQUE AND CONSEQUENTIAL.
Start from: systems/characters/character_generation_questionnaire_v30.md,
systems/characters/character_histories_v30.md, conviction_taxonomy_v30.md,
conviction_axis_matrix_v30.md, references/descriptor_registry.yaml (domain: actor - attributes,
aggregates, conviction weights, ethical axes, orientation scalars, personal tracks, templates),
systems/_architecture/player_agency_v30.md, systems/npcs/npc_behavior_v30.md,
systems/world/sim/npe.py (the NPC generator - what does it actually vary per NPC?),
registers/placeholder_names.yaml, and references/glossary/GLOSSARY_characters.md.
Interrogate:
  - what does the questionnaire elicit, and which of its answers has a descriptor, an owned-state
    row, or a key? Which are pure prose with no mechanical home?
  - npe.py generates NPCs: enumerate exactly which fields it varies and which it leaves constant.
    Two generated NPCs - how many ways can they actually differ, and does any of that difference
    change a resolution?
  - relationships, obligations, debts, rivalries, kinship, patronage: a character's distinctiveness
    is largely WHO THEY ARE TO OTHERS. Is there any relational descriptor or state anywhere?
  - a character's HISTORY as individuation (where they are from, what they did, who wronged them):
    conviction scars are the one implemented carrier. What else does canon assert and not carry?
  - skills, techniques, equipment, reputation: which are per-instance data and which are global?`,
  },
  {
    key: 'C2-faction-individuation',
    prompt: `Lane C2 - WHAT MAKES A FACTION UNIQUE AND CONSEQUENTIAL, AT EVERY TIER.
Start from: systems/factions/faction_state_authoring_v30.md (the authoring surface),
faction_canon_v30.md (the four canonical factions), faction_behavior_v30.md, faction_politics_v30.md,
engine/autoload/game_state.py STARTING_STATS (4 static instances - read exactly what differs),
systems/factions/sim/faction_action.py (the action dispatch and the faction-unique branch),
the six stub modules charter_liberties / hafenmark_equipment / home_sanctuary /
infrastructure_reclamation / varfell_mandate_action / varfell_territorial_acquisition,
systems/factions/factions_flow_skeleton_v1.md, and the faction_state / faction_politics rows in
references/module_contracts.yaml.
Interrogate:
  - the four factions differ by a stat block and by a faction-unique action dispatched on NAME.
    Hafenmark and Varfell have no unique action live and fall through to the universal fallback.
    Is faction identity DATA on the instance or a hardcoded branch? Name every hardcoded branch.
  - what would a fifth faction need in order to exist? Enumerate every authored field, and say
    which of them has no schema home. This is the sharpest test of whether individuation is data.
  - the design says factions emerge at settlement and provincial tiers (settlement_layer_v30.md
    sections 6.1-6.3 Stature Ladder; scale_hierarchy_v1.md section 5.1 rules the tiers independent).
    An emergent faction cannot be a hardcoded branch. What authoring schema would a tier-agnostic
    faction need - goals, methods, power basis, membership, territory, ideology - and which of
    those exists?
  - institutional_culture is a single per-faction scalar. Is one scalar enough to individuate a
    faction's BEHAVIOUR, or does faction_behavior_v30.md assert distinctions the schema cannot hold?
  - what individuates a faction's RELATIONSHIP to another faction (history, grievance, treaty,
    rivalry)? Treaties appear in no module's state block - is faction-to-faction relation authored
    anywhere at all?`,
  },
  {
    key: 'C3-settlement-and-world-individuation',
    prompt: `Lane C3 - WHAT MAKES A SETTLEMENT, A TERRITORY, AND THE WORLD UNIQUE AND CONSEQUENTIAL.
Start from: systems/settlements/valoria_geography_v30.yaml (the 37 authored settlements - read what
each row actually carries), systems/settlements/settlement_layer_v30.md sections 1.1-2.1,
territory_temperaments_v30.md, systems/settlements/sim/registry.py (the Settlement dataclass) and
temperaments.py (a verified zero-importer orphan - so temperament individuation is authored and
unread), systems/world/geography_v30.md, systems/world/worldbuilding_v30.md, the scenario_authoring
and settlement_layer and settlement_economy rows in references/module_contracts.yaml, and
proposals/ for any settlement-generator proposal (VSG).
Interrogate:
  - enumerate the per-settlement authored fields in valoria_geography_v30.yaml and, for each, find
    the code that reads it. A field nothing reads is flavour with no hook - list them all.
  - territory temperaments are authored and the module is an orphan. Is the gap a missing contract
    row (nobody owns temperament), a missing key (nothing announces a temperament expressing), or
    both?
  - what individuates a settlement beyond its four scalars - culture, trade, resource, faith,
    grievance, founding, hinterland? Which of those does canon assert and the schema not carry?
  - the scenario_authoring contract module: what is it FOR, what does it own, and can it author a
    starting world that differs from the shipped one? If not, the world is a singleton and every
    campaign starts identically - is that a design ruling or an unfilled gap? Cite, do not assume.
  - what makes the WORLD itself configurable: era, calamity state, starting clocks, invasion
    posture, which factions exist. Is there any world-authoring schema, or is world-gen a
    constant table in engine/autoload/game_state.py?
  - geography as individuation: adjacency, terrain, distance and chokepoints have real code and no
    contract module and no key scale. What individuating geographic fact can the schema not hold?`,
  },
]

const cFirst = await agent(COMMON + '\n\n' + LADDER + '\n\n' + CONFIG_COMMON + '\n\n' + C_LANES[0].prompt,
  { label: C_LANES[0].key, phase: 'Config', model: 'sonnet', effort: 'high', schema: GAP_SCHEMA })

const cRest = await parallel(C_LANES.slice(1).map(l => () =>
  agent(COMMON + '\n\n' + LADDER + '\n\n' + CONFIG_COMMON + '\n\n' + l.prompt,
    { label: l.key, phase: 'Config', model: 'sonnet', effort: 'high', schema: GAP_SCHEMA })))

const config = [cFirst].concat(cRest).filter(Boolean)
for (const r of config) run.lens('config:' + r.lane, r.findings)

const all = strata.concat(lenses).concat(config)
const flat = all.flatMap(r => (r.findings || []).map(f => Object.assign({}, f, { _lane: r.lane })))
run.round('agonist-total', flat)
log('agonist passes complete: ' + flat.length + ' raw findings from ' + all.length + ' lanes')

// P7b - rank by INDEPENDENT REDISCOVERY before the critics see anything, so the clusters handed to
// the antagonists are the corroboration groups rather than an arbitrary slice.
const ranked = hRediscover(flat, f => f._lane)
log('deduped to ' + ranked.length + ' distinct gaps; top rediscovery = ' +
  (ranked.length ? ranked[0].rediscovery : 0))

// ---------------------------------------------------------------------------------------------
// ANTAGONIST. Structural independence: hCritic() routes to .claude/agents/valoria-critic.md, whose
// tools list has no Write/Edit/Bash. The critics receive the producers' OUTPUT and never their
// reasoning - that is the relay, not a dialogue (CLAUDE.md section 10).
// ---------------------------------------------------------------------------------------------
phase('Adversarial')

const CLUSTERS = [
  { key: 'C1-lower-ladder', match: g => ['character', 'settlement', 'settlement_faction'].indexOf(String(g.findings[0].rung || '')) >= 0 },
  { key: 'C2-middle-ladder', match: g => ['territory', 'province', 'provincial_faction'].indexOf(String(g.findings[0].rung || '')) >= 0 },
  { key: 'C3-upper-ladder', match: g => ['national_faction', 'national_governance'].indexOf(String(g.findings[0].rung || '')) >= 0 },
]
const assigned = new Set()
const clusterSets = CLUSTERS.map(c => {
  const got = ranked.filter(g => g.findings.length && c.match(g))
  got.forEach(g => assigned.add(g.key))
  return { key: c.key, groups: got }
})
clusterSets.push({ key: 'C4-individuation-and-cross-rung', groups: ranked.filter(g => !assigned.has(g.key)) })

function renderGroups(groups) {
  return groups.map((g, i) => `--- CLAIM ${i + 1} (rediscovery ${g.rediscovery}, lanes: ${g.lenses.join(', ')})
claim: ${g.findings[0].claim}
gap_kind: ${g.findings[0].gap_kind} | rung: ${g.findings[0].rung} | lens: ${g.findings[0].lens}
proposal: ${g.findings[0].proposal}
evidence: ${g.findings[0].evidence}
existing_tracking: ${g.findings[0].existing_tracking} | producer confidence: ${g.findings[0].confidence}`).join('\n')
}

const critiques = await parallel(clusterSets.filter(c => c.groups.length).map(c => () =>
  run.attempt('Adversarial', agent(`You are the antagonist in a Valoria agonist->antagonist relay.
Twelve producer lanes swept the entity ladder, 18 domain lenses, and the individuation/authoring
surface against the Key type registry
(systems/_architecture/key_type_registry_v30.md, 55 types) and the module contracts
(references/module_contracts.yaml, 27 modules) looking for MISSING keys and contracts. Below is the
cluster of their output you are assigned. You never saw how they got there.

Rule per claim: uphold / overturn (false, or stale - the schema already carries it) / soften (real
but inflated, or already tracked - NAME the ED or PP or gap_note) / sharpen (worse than claimed).
Set 'target' to the claim text so the ruling binds to it.

The three ways these claims are most likely to be WRONG, in this corpus specifically:
  1. The concept exists under another name in an adjacent subsystem. This corpus keeps things
     where you would not look. Grep the concept, not the term.
  2. The schema DOES carry it and the producer read a generated view instead of the authored
     source. references/KEY_INDEX.md and CONTRACT_INDEX.md are joins; a blank cell there means
     'not declared', which is NOT the same claim as 'none'. Open the registry and the yaml.
  3. It is already filed. 31 open items in registers/editorial_ledger*.jsonl touch keys, contracts
     or schema, and most module rows carry their own gap_notes. An already-tracked gap is a soften,
     not an uphold.
Also check the reverse failure: a proposal that special-cases a named entity, or invents a
scale-local dialect, instead of composing on an existing primitive. That is a defect in the
proposal even when the gap is real.

Then HUNT WHAT THEY MISSED. Read at least one surface this cluster does not cite - the obvious
candidates are systems/_architecture/{key_substrate_v30,propagation_spec_v1,scale_transitions_v30}.md,
references/descriptor_registry.yaml, references/ENGINE_ATLAS.md and the per-subsystem
*_flow_skeleton_v1.md section 7 gap lists. Put what you find in 'missed'.

Cross-domain rule: if a claim sits outside this cluster's rungs, report what you saw and do NOT
rule on it - the harness records it as a terminal observation.

CLUSTER ${c.key}:
${renderGroups(c.groups)}`,
    hCritic({ label: 'critic:' + c.key, phase: 'Adversarial', model: 'opus', effort: 'high', schema: CRITIC_SCHEMA })))))

const verdicts = critiques.filter(Boolean).flatMap(c => c.verdicts || [])
const missed = critiques.filter(Boolean).flatMap(c => c.missed || [])
for (const c of critiques.filter(Boolean)) run.lens('critic:' + (c.coverage || '').slice(0, 40), c.verdicts)
run.critiqued('Adversarial', ranked.length, clusterSets.filter(x => x.groups.length).reduce((n, x) => n + x.groups.length, 0))

// P8 - every non-uphold verdict is a recorded disagreement, built by the owner's helper so the
// record actually carries its call site (the wave-script defect hVerdictDispute exists to prevent).
for (const v of verdicts) {
  if (!v || v.verdict === 'uphold') continue
  const g = ranked.find(x => x.findings.length && hSameFinding(x.findings[0], { claim: v.target, evidence: v.evidence }))
  run.dispute(hVerdictDispute(v, 'valoria-critic', (g && g.findings[0].claim) || String(v.target || '')))
}
log('critics returned ' + verdicts.length + ' verdicts (' +
  verdicts.filter(v => v && v.verdict === 'overturn').length + ' overturn) and ' + missed.length + ' missed items')

// ---------------------------------------------------------------------------------------------
// SYNTHESIS. Opus, because this is the stage that GATES the result: it decides what survives, and
// a wrong call here is the one that reaches the register.
// ---------------------------------------------------------------------------------------------
phase('Synthesis')

const synth = await agent(`Synthesize the Valoria world-schema gap audit into a single ranked
register. You are the stage that gates the result; everything below has already been produced and
adversarially checked, and your job is to decide what survives and how it is stated.

RANKED GAPS (deduped across THREE method-disjoint decompositions of the same subject: a strata
pass that walked the entity ladder rung by rung, a lens pass that swept 18 domain lenses across
every rung at once, and a config pass that asked what must be AUTHORED for an instance to be unique
and consequential. 'rediscovery' counts INDEPENDENT lanes; a gap reached by lanes from different
passes is corroborated by disjoint METHOD, which is worth materially more than two lanes of the
same pass reaching it):
${JSON.stringify(ranked.map(g => ({ rediscovery: g.rediscovery, lanes: g.lenses, f: g.findings[0] })), null, 1)}

CRITIC VERDICTS (read-only valoria-critic agents that never saw the producers' reasoning):
${JSON.stringify(verdicts, null, 1)}

WHAT THE CRITICS SAY THE PRODUCERS MISSED:
${JSON.stringify(missed, null, 1)}

RULES FOR THE REGISTER:
  - Apply the verdicts. An overturned claim does NOT enter the register; say so in residuals with
    the reason. A softened claim enters at its reduced severity with its ED named. A sharpened one
    enters as sharpened.
  - Rank by rediscovery first, then by how much of the ladder the gap blocks. Assign G-01, G-02...
  - Disposition every row: propose_key / propose_contract / already_tracked / needs_jordan_ruling /
    not_a_gap. A gap that requires a design CALL (which of the 8 consumerless keys are terminal;
    whether a faction tier is a field or a module; whether the B12 Territory tier enters the scales
    enum) is needs_jordan_ruling and goes in held_for_jordan - this audit does not rule.
  - Each propose_key row states the concrete type_id, family, required_payload_fields and
    default_scale_signature. Each propose_contract row states the exact module/field/row. Compose on
    existing primitives; a proposal that special-cases an entity is a defect - drop it and say why.
  - NOTE, prominently, that key_type_registry section 10 forbids appending any new key type without
    a row in references/rendering_dispositions.yaml, which does not exist. Every propose_key row is
    therefore blocked on that file being created. That is itself a register row.
  - residuals: state plainly what this run did NOT cover. Lanes that returned nothing, surfaces
    nobody read, lenses that got thin treatment. Do not smooth it over - a reader must be able to
    tell a clean surface from an unread one.
  - The config pass introduces a distinct class of gap: an entity that the schema can track
    perfectly and cannot INDIVIDUATE. Keep those rows visibly separate in the register (gap_kind
    missing_authoring_schema / missing_individuation_descriptor, disposition propose_descriptor /
    propose_authoring_field) - a reader must be able to see which gaps stop the engine from
    working and which stop it from producing a world worth playing twice. Every hardcoded-singleton
    finding (identity written as a named branch in code rather than data on the instance) is
    scripting drift and ranks high regardless of rediscovery count.
  - ladder_verdict: three or four sentences on (a) whether the schema can express the ratified
    entity ladder at all and where exactly it breaks, and (b) whether it can individuate the
    entities it does carry, or whether the world is a set of near-identical instances plus a few
    hardcoded singletons.`,
  { label: 'synthesis', phase: 'Synthesis', model: 'opus', effort: 'xhigh', schema: SYNTH_SCHEMA })

for (const v of verdicts) {
  if (!v || v.verdict === 'uphold') continue
  run.adjudicate(String(v.target || ''), 'synthesis applied the ' + v.verdict + ' verdict when building the register', 'synthesis')
}
for (const d of run.disagreements) {
  if (d.status === 'open') run.adjudicate(d.finding_id, 'carried into the register at the critic-assigned severity; no counter-evidence was produced', 'synthesis')
}

return {
  summary: run.summary(),
  raw_findings: flat.length,
  distinct_gaps: ranked.length,
  rediscovery_top: ranked.slice(0, 12).map(g => ({ n: g.rediscovery, lanes: g.lenses, claim: g.findings[0].claim })),
  lane_coverage: all.map(r => ({ lane: r.lane, n: (r.findings || []).length, clean: (r.clean || []).length, coverage: r.coverage })),
  critic_missed: missed,
  register: synth,
}
