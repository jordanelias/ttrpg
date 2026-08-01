export const meta = {
  name: 'wave3-keys',
  description: 'W3 of the code-shape program (ED-IN-0091/ED-IN-0096): Keys & contract truth — combat-pair consumers, contract sweep, scalar registration, live causes[], silent-emitter declaration, W2 handoffs (accord-echo Key type + province-Accord drift probe)',
  phases: [
    { title: 'Build', detail: '4 parallel file-disjoint lanes: consumers+causes · contract sweep · scalars · silent emitters', model: 'sonnet' },
    { title: 'Handoff', detail: 'W2 handoffs: scene.accord_echo registration + queue-parity + province-Accord report-only drift probe', model: 'sonnet' },
    { title: 'Adjudicate', detail: 'emit-closure re-run: no new dangling emit, every declared consumer real or ruled', model: 'opus' },
    { title: 'Critic', detail: 'read-only adversarial relay over the wave diff', model: 'opus' },
    { title: 'Bookkeeping', detail: 'ED-IN-0096 + ED-WR-0010 + execution ledger + HANDOFF_IN', model: 'sonnet (effort low)' },
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
// Harness block inserted/synced by: python tools/ci_wf_harness_check.py --fix

// ---------------------------------------------------------------------------------------------
// W3 executes 01_orchestration_plan_v1.md §3 Wave 3, as re-scoped by the 2026-07-29 G12 preflight
// (each correction verified in-tree; they OVERRIDE the plan where they conflict):
// - CONSUMER PRIMITIVE: consumers use TickScheduler.subscribe(type_id, cb) (keys.py:447), not the
//   emitter-side apply= kwarg. The one live consumer pattern is articulation._make_trigger_callback.
// - npc_behavior HAS NO RUNTIME (systems/npcs/ has zero .py files). Its causes[]/private_observers
//   "emit sites" are design-doc pseudocode in political_dynamics_keys_migration_v30.md. No wave
//   item builds that module (fork 9 / WR). causes[] is wired at LIVE emitters only.
// - 4TH DANGLING EMIT discovered: mechanical.season_change (engine_clock, contracts:715) — the
//   register never named it. engine_clock is fork-3-gated (ED-1051, sole T0): the emit's consumer
//   decision HOLDS AT FORK 3 with a loud deviation record. W3 exit is therefore "4 → 2 dangling,
//   both explicitly fork-held (env.crisis fork 4; season_change fork 3)" — NOT the plan's ≤1.
// - OI-40a scale-vocabulary unification is HELD: the concurrent centralization program
//   (ED-IN-0103, audit/2026-07-29-centralization-single-owner/) carries it as its §6 fork 1 for
//   Jordan. W3 records the cross-program coordination row and touches nothing. (The register's
//   "A8" citation is unverifiable — G12 correction recorded.)
// - Province-Accord recompute would OVERWRITE live direct Territory.accord writes
//   (parliamentary_transfer.py:210, mass_seizure.py:295) — a write-model design reconciliation
//   belonging to SE's L/PS workstream (OI-37). W3 ships a REPORT-ONLY drift probe, no write.
// - MS ownership: declare MS in peninsular_strain's state: block ONLY; GAP-F1's env.ms_delta emit
//   would itself be a new dangling emit — recorded as residual, not added.
// - Seam stops unchanged: systems/combat/**, combat_engine_v1/wrapper.py, faction_action.py:349,
//   references/id_reservations.yaml, registers/review_baseline.yaml. No golden may move (this
//   wave declares NO re-record; any moved pin is a stop).
// - PC's wrapper_emit_key_map.md has NOT landed — item-1 registry-side work proceeds; the
//   consumption is recorded outstanding (plan's own term), never guessed.
// - File ownership (disjoint): L-consumers -> engine/cross_scale/{articulation,echo_transport,
//   parliamentary_bridge}.py + systems/articulation/articulation_layer_v30.md + engine/tests/;
//   L-contracts -> references/module_contracts.yaml (sole editor) ; L-scalars ->
//   references/descriptor_registry.yaml (sole editor) + tests/valoria/; L-silent ->
//   systems/_architecture/key_type_registry_v30.md (sole editor) + the four modules' design-doc
//   emit notes; HANDOFF stage -> engine/cross_scale/echo_transport.py (after L-consumers returns)
//   + systems/overview/sim/accounting.py + key_type_registry additions coordinated with L-silent
//   via oracle_requests (the registry file's edits are merged by L-silent's owner role — the
//   Handoff stage passes its registration REQUEST to bookkeeping if L-silent has closed).
//   Oracle file (test_pipeline_reach.py): edited ONLY by L-consumers (retiring diagonal-causes).
// ---------------------------------------------------------------------------------------------

const run = hRun('wave3-keys')

const LANE_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['files_touched', 'tests_added', 'falsifier', 'golden_status', 'stopped_items', 'oracle_requests', 'notes'],
  properties: {
    files_touched: { type: 'array', items: { type: 'string' } },
    tests_added: { type: 'array', items: { type: 'string' } },
    falsifier: { type: 'string' },
    golden_status: { type: 'string' },
    stopped_items: { type: 'array', items: { type: 'string' } },
    oracle_requests: { type: 'array', items: { type: 'string' } },
    notes: { type: 'string' },
  },
}

const ADJ_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['verdict', 'closure_findings', 'dangling_census', 'notes'],
  properties: {
    verdict: { enum: ['closed', 'closed-with-residuals', 'open-defects'] },
    closure_findings: { type: 'array', items: { type: 'string' } },
    dangling_census: { type: 'array', items: { type: 'string' } },
    notes: { type: 'string' },
  },
}

const CRITIC_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['verdicts', 'missing'],
  properties: {
    verdicts: {
      type: 'array',
      items: {
        type: 'object', additionalProperties: false,
        required: ['target', 'verdict', 'severity', 'evidence'],
        properties: {
          target: { type: 'string' },
          verdict: { enum: ['uphold', 'overturn', 'soften', 'sharpen'] },
          severity: { enum: ['high', 'medium', 'low'] },
          evidence: { type: 'string' },
        },
      },
    },
    missing: { type: 'array', items: { type: 'string' } },
  },
}

const COMMON = `Repo /home/user/ttrpg. Read CLAUDE.md §0/§0.1, then
audit/2026-07-29-code-shape-open-items/01_orchestration_plan_v1.md §3 Wave 3 + this script's
header corrections (they OVERRIDE the plan; each is an in-tree-verified G12 correction) +
00_open_items_register.md for your OI rows. Claims are LEADS — re-verify at cited file:line.
No invented constants/types/consumers — every addition cites canon (PP/ED/§) and every new emit
declaration is paired with a real consumer or an explicit fork-held disposition IN THE SAME EDIT
(never a new dangling emit). Do NOT edit files another lane owns (header ownership map). This
wave declares NO golden re-record: if anything you do moves a pinned golden, STOP that item.
STOP-list: systems/combat/**, wrapper.py, faction_action.py:349, id_reservations.yaml,
review_baseline.yaml. Report per LANE_SCHEMA; put oracle/registry cross-lane needs in
oracle_requests.`

phase('Build')

const CONSUMERS_PROMPT = `${COMMON}

Lane: OI-22a + OI-27a slice + OI-28's LIVE half (W3 items 1+5, re-scoped).
1. COMBAT-PAIR CONSUMERS: the registry (key_type_registry_v30.md:727-742) declares consuming
   systems [npc_behavior, faction_layer, articulation] for scene.combat_resolved/felled;
   articulation is the one with runtime. Execute ED-IN-0004's slice: add the two combat trigger
   rows to systems/articulation/articulation_layer_v30.md §3.1 (per its existing row format,
   citing ED-IN-0004 + the registry's declared consumption — this executes an already-filed ED,
   not new canon), and extend articulation.py's _TRIGGER_TYPE_IDS + subscribe_all to 13 types
   (stub-flag callbacks, same pattern). Update the test to >= 13.
2. CONTRACT consumes: truth — coordinate via oracle_requests: request L-contracts add
   scene.combat_resolved/felled to npc_behavior + faction_state consumes: lists (declared intent
   per the registry; their runtime wiring stays gated on their builds — fork 9 / module builds).
3. OI-28 LIVE causes[]: wire causes[] at the live emitters where a genuine upstream Key exists —
   in parliamentary_bridge/echo_transport, when an echo Key is emitted for a scene that itself
   emitted a scene Key in the same season flow, the echo Key's causes[] carries that scene Key's
   uuid (keys.py:325 invariant: causes[] references keys already in the log — verify ordering).
   Cite political_dynamics_keys_migration_v30.md §5.4's pattern as the authoring guidance. Do NOT
   touch the npc_behavior pseudocode sites (no runtime — recorded design-gated).
4. ORACLE (you are this wave's sole test_pipeline_reach.py editor): retire/flip the
   diagonal-causes row (OI-28) with a strict assertion that a seeded campaign (echo flags ON)
   emits >= 1 Key with non-empty causes[] referencing an in-log uuid (assert checked >= 1).
5. Tests: subscription count; causes[] end-to-end through TickScheduler in a seeded run.
golden_status: the causes[] field addition must not change any pinned key_log_hash — check which
pins hash keys (test_parliamentary_bridge _ON_KEYLOG_HASH!) and if the hash covers causes[],
that pin moves — STOP and report rather than re-record (no re-record is declared this wave).
Return per LANE_SCHEMA.`

const CONTRACTS_PROMPT = `${COMMON}

Lane: OI-24 + OI-32a + OI-40a coordination (W3 item 3, re-scoped). You are the SOLE editor of
references/module_contracts.yaml this wave.
1. npc_behavior: fix the inline-comment/gap_note contradiction (:149-152 comments still claim
   four types are "NOT in registry" while gap_notes:179 records ED-935 registered them — verify
   in key_type_registry_v30.md which is true, then make comments+gap_notes agree with the tree).
2. doc: repoint (C-KEY-2): npc_behavior's doc: points at the Key-silent npc_behavior_v30.md
   while the real Key-sequencing spec (political_dynamics_keys_migration_v30.md) sits in
   sources:. Repoint doc: to the keys-migration spec AND keep the behavioral doc in sources:
   (both remain reachable; cite C-KEY-2).
3. faction_politics state: block — read systems/factions/faction_politics_v30.md's actual
   Standing ladder / coup / succession definitions and declare the top-level state items
   (name, bucket, writable, formula-pointer per the file's own state: row format elsewhere);
   contract truth only, no sim (the sim build is DEFERRED → FA per §3.5).
4. MS ownership (OI-32a): add MS to peninsular_strain's state: block (ownership declaration,
   citing GAP-F1 + the live tick at systems/overview/sim/{ms_track,accounting}.py); do NOT add
   an env.ms_delta emit (it would be a new dangling emit — record as GAP-F1 residual note in
   gap_notes). Also fix victory's g_ms0 annotation ("unowned clock") to point at the new owner.
5. Per oracle_requests from the consumers lane: add scene.combat_resolved/felled to
   npc_behavior + faction_state consumes: lists (declared intent; runtime gated on builds).
6. OI-40a: NO vocabulary unification (held at the centralization program's §6 fork 1,
   ED-IN-0103) — add ONE coordination comment at the contracts' scales: field documentation
   point (if one exists) citing the held fork; nothing else.
Tests: extend the existing contract-validation test coverage minimally if a schema-shaped test
exists (find it); otherwise validation = the contract-conformance CI check passing.
Return per LANE_SCHEMA.`

const SCALARS_PROMPT = `${COMMON}

Lane: OI-30a (W3 item 4). You are the SOLE editor of references/descriptor_registry.yaml.
Register the Category-B scalars (07-14 unification §3 / ED-IN-0059 list): Wounds, Turmoil,
Accord, Poise, Initiative, and the engine_clock season counter. The registry's KIND enum has no
category for personal combat tracks — extend the enum minimally (e.g. one new kind
'personal_track' or reuse-if-adequate; ONE new kind maximum, not one per scalar) and add each
entry with its canonical home pointer (find each scalar's defining doc/contract row: Wounds/
Poise/Initiative are bucket:track in personal_combat's contract :834-837; Turmoil in
peninsular_strain state:; Accord per settlement_layer/§5.5; season counter per engine_clock —
note its fork-3 gate in the entry comment). Respect the roster-IN-FLUX warning (CLAUDE.md §5):
these are REGISTRATIONS with pointers, not schema bindings — say so in the section comment.
C2 (npc beliefs/concerns/projects) stays J (§5 fork 11) — untouched. Test: if
tests/valoria has a descriptor-registry schema test, extend it for the new kind; else add a
minimal known-answer parse test. Return per LANE_SCHEMA.`

const SILENT_PROMPT = `${COMMON}

Lane: OI-25 (W3 item 7, ED-IN-0014). You are the SOLE editor of
systems/_architecture/key_type_registry_v30.md this wave (the Handoff stage will REQUEST one
more registration from you via the orchestrator — scene.accord_echo; add it per its request in
oracle_requests when you see it in your prompt's addendum, else leave to bookkeeping).
For the four silent emitters — settlement_layer (g_ord0 revolt / g_def0 auto-capture gates),
ci_political, victory (era/occupation transitions), territorial_piety:
1. Register the new Key types in key_type_registry_v30.md per the §1 format (mirror
   scene.combat_resolved's entry shape :727-742): e.g. state.revolt_triggered,
   state.settlement_captured, state.era_transition, state.theocracy_attempt (derive each name
   from the module's own canon doc — read the gate's section and cite it; do not invent
   semantics beyond what the gate already does).
2. Declare the emits in references/module_contracts.yaml — COORDINATE: the contracts lane owns
   that file; put the exact emit rows you need into oracle_requests for the orchestrator to
   route (do not edit the file yourself).
3. CONSUMER RULE (binding): every new type's consuming_systems names articulation (the live
   chronicle subscriber — extend its subscription is the consumers lane's file; put the type_ids
   into oracle_requests for them) or carries an explicit fork/docket-held disposition line in
   the registry entry. NEVER a new dangling emit.
4. The EMITTING modules have varying runtime (settlement_layer sim exists; victory exists;
   ci_political/territorial_piety are deferred) — for runtime-less emitters the registration +
   contract declaration is the deliverable (emit fires when the module builds); for
   settlement_layer/victory, wire the actual sched.emit at the gate site ONLY if the gate is
   reachable in the live loop AND no pinned golden moves (check; else declare-only and record).
Tests: registry-parse coverage for the new entries (the existing registry parser test — find it).
Return per LANE_SCHEMA.`

const [consumersL, contractsL, scalarsL, silentL] = await parallel([
  () => agent(CONSUMERS_PROMPT, { schema: LANE_SCHEMA, label: 'build:consumers+causes', phase: 'Build', model: 'sonnet', effort: 'high' }),
  () => agent(CONTRACTS_PROMPT, { schema: LANE_SCHEMA, label: 'build:contract-sweep', phase: 'Build', model: 'sonnet', effort: 'high' }),
  () => agent(SCALARS_PROMPT, { schema: LANE_SCHEMA, label: 'build:scalar-registration', phase: 'Build', model: 'sonnet', effort: 'low' }),
  () => agent(SILENT_PROMPT, { schema: LANE_SCHEMA, label: 'build:silent-emitters', phase: 'Build', model: 'sonnet', effort: 'high' }),
])

run.lens('build:consumers+causes', consumersL ? [consumersL] : [])
run.lens('build:contract-sweep', contractsL ? [contractsL] : [])
run.lens('build:scalar-registration', scalarsL ? [scalarsL] : [])
run.lens('build:silent-emitters', silentL ? [silentL] : [])

phase('Handoff')

const HANDOFF_PROMPT = `${COMMON}

Lane: the two W2 handoffs (executes what W2 deferred here). Lane outputs you may need:
CONSUMERS: ${JSON.stringify(consumersL)}
SILENT: ${JSON.stringify(silentL)}
1. scene.accord_echo REGISTRATION + QUEUE PARITY: register scene.accord_echo in
   key_type_registry_v30.md per the §1 format (coordinate with the silent-emitters lane's edits —
   they own the file this wave; if their diff already landed, append compatibly; emitting_systems
   [echo_transport §5.5 leg], consuming_systems [articulation] — and put the articulation
   subscription need into oracle_requests if the consumers lane didn't already cover it). Then
   refactor echo_transport's _apply_accord_echo to route through the scheduler
   (sched.emit(key, apply=...) with the settlement-Order write inside the apply closure — OF-7
   deferred apply at accounting_boundary), restoring queue-parity with the domain echo and
   retiring the W2 'applied immediately' rename (update both docstrings; keep accord_applied's
   name only if semantics still warrant it — if now queued, rename accordingly and fix the W2
   comment trail). The leg is DORMANT (no live producer declares scene_outcome) so no golden can
   move — verify by running the campaign-golden tests.
2. PROVINCE-ACCORD DRIFT PROBE (report-only, NO write): add a step to
   systems/overview/sim/accounting.py's run_accounting that computes
   registry.province_accord(pid) per province and RECORDS divergence from the live
   Territory.accord value into campaign telemetry (mirror the stub_hits pattern — additive field,
   zero/absent when no divergence or no settlements), WITHOUT writing either value. Cite the W2
   re-critic finding + OI-37/SE routing for the write-model reconciliation. Tests: a seeded
   campaign where a settlement Order diverges from Territory.accord surfaces a nonzero probe
   value (assert checked >= 1); the probe's presence moves NO pinned golden (verify — additive
   telemetry only; if CampaignResult shape pins exist, mirror how stub_hits avoided them).
Return per LANE_SCHEMA.`

const handoffL = await agent(HANDOFF_PROMPT, { schema: LANE_SCHEMA, label: 'handoff:accord-key+drift-probe', phase: 'Handoff', model: 'sonnet', effort: 'high' })
run.lens('handoff:accord-key+drift-probe', handoffL ? [handoffL] : [])

phase('Adjudicate')

const adj = await agent(`${COMMON}

Opus adjudication (module-adjudicator emit-closure method, read-only — name fixes, don't make
them). Re-run the emit-closure census over references/module_contracts.yaml + the registry on
the CURRENT tree:
1. DANGLING CENSUS (the exit metric): enumerate every emit with zero named consumers. The wave's
   re-scoped exit is "exactly 2, both fork-held (env.crisis → fork 4; mechanical.season_change →
   fork 3)". Any OTHER dangling emit — including any NEW type this wave registered without a
   consumer-or-disposition — is a defect. Fill dangling_census with the full list.
2. Every new registry entry: canon-cited (the gate/section it derives from), consumer named and
   REAL (articulation's list actually extended?) or explicitly fork-held in the entry.
3. The causes[] wiring: does the uuid ordering respect keys.py:325's in-log invariant? Is the
   causal edge genuine (echo caused by scene key) rather than decorative?
4. The queue-parity refactor: does the accord apply now genuinely run at accounting_boundary
   (OF-7)? Did the rename trail get cleaned at both ends?
5. Contract sweep: does faction_politics' new state: block match its canon doc (spot-check the
   Standing ladder rows against faction_politics_v30.md)? Is the MS declaration consistent with
   the live tick site? Emit-closure percentage vs the 2026-07-13 97.9% precedent, residual named.
LANE OUTPUTS: ${JSON.stringify({ consumersL, contractsL, scalarsL, silentL, handoffL })}`,
  { schema: ADJ_SCHEMA, label: 'adjudicate:w3', phase: 'Adjudicate', model: 'opus', effort: 'high' })
run.lens('adjudicate:w3', adj && adj.closure_findings ? adj.closure_findings : [])

phase('Critic')

const critic = await run.attempt('critic:w3',
  agent(`Adversarial critic relay for Wave 3 (repo /home/user/ttrpg; judge from file contents).
Producers' OUTPUT only. Break the wave against 01_orchestration_plan_v1.md §3 Wave 3's exit +
§0.1 + the script-header re-scopes:
1. NO-NEW-DANGLING rule: grep every type this wave added to the registry/contracts — does each
   have a real consumer (articulation's _TRIGGER_TYPE_IDS actually contains it?) or an explicit
   fork-held line? Cross-check the adjudicator's dangling_census independently.
2. FABRICATION HUNT: every new Key type name/semantics traced to the emitting module's own canon
   section; every scalar registration's home pointer real; the faction_politics state: rows
   present in the canon doc.
3. GOLDEN SAFETY: this wave declares NO re-record — run-compare impossible for you, so verify
   structurally: does causes[] enter any hashed key-log pin? does the drift probe or queue-parity
   change any pinned field?
4. HONESTY: the two loud deviation records (season_change → fork 3; OI-40a held at ED-IN-0103's
   fork) present in the execution ledger? The unverifiable "A8" citation recorded?
5. What is MISSING vs the exit criteria (adjudicator BEFORE/AFTER, the ≥1 consumed
   scene.combat_resolved campaign assertion — note the pair is consumed by articulation
   subscription; is there a test asserting a combat key actually reaches the subscriber under
   the flag, or is it honestly xfail-gated on DISPATCH_COMBAT_BRIDGE?).
Finding nothing is a real verdict.
PRODUCER OUTPUT: ${JSON.stringify({ consumersL, contractsL, scalarsL, silentL, handoffL, adj })}`,
    hCritic({ schema: CRITIC_SCHEMA, label: 'critic:w3', phase: 'Critic', model: 'opus', effort: 'high' })))

run.critiqued(['build:consumers+causes', 'build:contract-sweep', 'build:scalar-registration', 'build:silent-emitters', 'handoff:accord-key+drift-probe'])
run.lens('critic:w3', critic && critic.verdicts ? critic.verdicts : [])

const overturns = (critic && critic.verdicts ? critic.verdicts : []).filter(v => v.verdict !== 'uphold')
for (const v of overturns) {
  // Built by the owner, not by hand: the four keys this call used to pass ({layer,target,
  // detail,severity}) are none of them keys run.dispute() reads, so every dispute this
  // script ever recorded was keyed '?' and could not be adjudicated. See hVerdictDispute.
  run.dispute(hVerdictDispute(v, 'critic:w3', v.target))
}

const ranked = hRediscover(
  [
    ...(critic && critic.verdicts ? critic.verdicts.map(v => ({ desc: v.target + ': ' + v.evidence, lens: 'critic' })) : []),
    ...(adj && adj.closure_findings ? adj.closure_findings.map(f => ({ desc: f, lens: 'adjudicator' })) : []),
  ],
  f => f.lens,
)

phase('Bookkeeping')

const book = await agent(`${COMMON}

Bookkeeping for Wave 3, AFTER the critic (disputes are the orchestrator's; mark disputed items
'pending orchestrator adjudication'). Edit ONLY: the execution ledger, registers/
editorial_ledger_in.jsonl + editorial_ledger_wr.jsonl, registers/handoffs/HANDOFF_IN.md, root
HANDOFF.md. Allocate ED-IN-0096 (W3 umbrella) and — only if OI-31b doc work landed — ED-WR-0010,
from the reserved blocks (id_reservations.yaml FROZEN; record in ledgers + execution ledger).
Rows for: OI-22a (consumers via articulation, ED-IN-0004 executed), OI-24 (a/b/c/d with the
npc_behavior comment-contradiction correction), OI-25 (types registered, consumers/dispositions),
OI-28 (live causes[] + design-gated pseudocode sites recorded), OI-30a (scalars + new kind),
OI-32a (MS declared; env.ms_delta residual), OI-40a (HELD at ED-IN-0103 §6 fork 1 — loud
coordination row; "A8" citation unverifiable), the season_change discovery (4th dangling emit,
HELD at fork 3 — loud deviation row: exit is 4→2-both-held, not the plan's ≤1), the two W2
handoffs (accord-echo type + queue parity; drift probe report-only, write-model → SE/OI-37),
PC emit-map consumption still outstanding. HANDOFF_IN: W3 landed, next = W4 (centralization).
Validate all JSONL parses + register sizes (archive uncited resolved entries per the established
procedure if the IN ledger exceeds its cap). Return per LANE_SCHEMA.`,
  { schema: LANE_SCHEMA, label: 'bookkeeping', phase: 'Bookkeeping', model: 'sonnet', effort: 'low' })
run.lens('bookkeeping', book ? [book] : [])

return {
  run: run.summary(),
  consumersL, contractsL, scalarsL, silentL, handoffL, adj, critic, ranked, book,
  orchestrator_note: 'Gate: adjudicate disputes -> fix batch if needed -> re-critic if substantive -> full suites + validators (NO golden may move) -> commit/PR/merge on CI green.',
}
