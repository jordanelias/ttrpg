export const meta = {
  name: 'wave2-seams',
  description: 'W2 of the code-shape program (ED-IN-0091/ED-IN-0095): orphan closure at the seams — accord echo, territory transfer, NPC/knot/settlement world chains, vertical-up handoff, articulation subscriber, OI-12 census — with a declared IN-family golden re-record',
  phases: [
    { title: 'Seams', detail: '5 parallel file-disjoint lanes: echo · transfer · handoff · articulation · OI-12 census', model: 'sonnet' },
    { title: 'World', detail: 'sole mc_v18/game_state writer: NPC generation + world chains + the DECLARED golden re-record', model: 'sonnet' },
    { title: 'Oracle', detail: 'single owner of test_pipeline_reach.py: flip W2 manifest rows to strict, add subscriber/census rows', model: 'sonnet' },
    { title: 'Adjudicate', detail: 'emit-closure + transfer-path + echo-semantics adjudication', model: 'opus' },
    { title: 'Critic', detail: 'read-only adversarial relay over the whole wave diff', model: 'opus' },
    { title: 'Bookkeeping', detail: 'per-lane EDs (IN/FA/WR/SE from reserved blocks) + execution ledger + HANDOFF_IN', model: 'sonnet (effort low)' },
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
// W2 executes 01_orchestration_plan_v1.md §3 Wave 2, as corrected by the 2026-07-29 G12 preflight:
// - PLAN CITATION CORRECTED: OI-03's spec is scale_transitions_v30.md §5.5 "Accord Domain Echo"
//   (lines ~208-221), NOT "LPS-2e" (which is the Mandate aggregate — a different mechanism). The
//   plan's citation is stale; record the correction, cite §5.5.
// - OI-04: the ONLY auto-populated casus belli is crown_constitutional_restoration (Crown, <6
//   territories). Wire the motion path against the existing CB machinery; NEVER invent CB
//   sources — if the seeded campaign cannot reach a transfer, the honest outcome is a wired
//   path + a recorded reachability note, not a fabricated CB.
// - OI-05 is THE declared IN-family golden re-record, and it spans EVERY campaign-golden file
//   whose pinned values derive from the seeded RNG stream: test_f7_smoke_oracle.py (seed 42),
//   test_mc_v18_regression.py (seed 0), and test_echo_transport.py / test_parliamentary_bridge.py
//   if their pins move. OLD values preserved in comments; full before/after table in the PR body.
//   G11: this is the one golden-moving PR in flight in the IN family.
// - keys.py SCALES is ("personal","settlement","territory","peninsula") — no oracle assertion may
//   construct a Key outside it (validator raises).
// - File ownership (no worktrees needed): L-echo -> engine/cross_scale/{echo_transport,domain_echo}.py;
//   L-transfer -> engine/cross_scale/parliamentary_bridge.py + systems/factions/sim/*;
//   L-handoff -> engine/cross_scale/{scene_dispatch,handoff_rules}.py; L-artic ->
//   engine/cross_scale/articulation.py + tests/valoria/test_articulation_subscriber.py (new);
//   L-census -> ledger/registers docs only; WORLD -> engine/mc_v18.py + engine/autoload/game_state.py
//   + systems/world/sim/npe.py + systems/{settlements,fieldwork}/sim wiring + the golden test files;
//   ORACLE stage is the SOLE editor of engine/tests/test_pipeline_reach.py.
// - Seam stops (unchanged): systems/combat/**, combat_engine_v1/wrapper.py, faction_action.py:349,
//   references/id_reservations.yaml, review_baseline.yaml (no protocol pre-declared this wave).
// ---------------------------------------------------------------------------------------------

const run = hRun('wave2-seams')

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
  required: ['verdict', 'closure_findings', 'notes'],
  properties: {
    verdict: { enum: ['closed', 'closed-with-residuals', 'open-defects'] },
    closure_findings: { type: 'array', items: { type: 'string' } },
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
audit/2026-07-29-code-shape-open-items/01_orchestration_plan_v1.md §3 Wave 2 (your governing spec)
+ 00_open_items_register.md for your OI rows + this script's header-comment corrections (they
override the plan where they conflict — each is a verified G12 correction). Register/plan claims
are LEADS: re-verify at the cited file:line before acting; adapt and record staleness rather than
executing it verbatim. No invented constants/actors/values — every derivation cites its canon
(PP/ED/§). Converted stubs return typed no-ops via engine.substrate.stubwire. Do NOT edit
engine/tests/test_pipeline_reach.py (the Oracle stage owns it) — put every manifest-row flip or
new-row need into oracle_requests. If your task would require touching systems/combat/**,
combat_engine_v1/wrapper.py, faction_action.py:349, references/id_reservations.yaml, or
registers/review_baseline.yaml: STOP that item into stopped_items and continue. golden_status
must state plainly whether anything you did can move a pinned golden.`

phase('Seams')

const ECHO_PROMPT = `${COMMON}

Lane: OI-03 — wire compute_accord_echo (the bottom-up settlement→province Accord write source,
zero callers). Spec = scale_transitions_v30.md §5.5 (the header correction; the module's own
docstring already cites it). Work:
1. Build the missing outcome-classification step at the echo boundary: a single-owner function in
   engine/cross_scale/echo_transport.py mapping a resolved scene to §5.5's scene_outcome vocabulary
   ('governance'|'destabilisation'|'territorial_transfer'|'violence') — derive ONLY from fields the
   scene already carries (scene_type, degree, echo block); cite §5.5 per mapping row; anything
   unmappable returns None and is recorded (never guessed).
2. Call compute_accord_echo from the echo path (mirroring how compute_domain_echo is called at
   echo_transport.py:132), applying its AccordEchoResult per its own dataclass semantics.
3. Tests (tests/valoria or engine/tests, NOT test_pipeline_reach.py): known-answer per §5.5 row —
   governance Success ⇒ Accord +1 on the right territory; violence ⇒ RS −1 + Accord −1; unknown
   pair ⇒ fires=False recorded. assert-that-asserted on any loop.
4. golden_status: state whether the new call can fire in the CURRENT seeded campaigns (if echoes
   only fire under ECHO_TRANSPORT/flags, say which flags gate it and whether any pinned golden
   moves — if one would, coordinate via oracle_requests/notes instead of re-recording yourself;
   the World lane owns this wave's re-record).
Return per LANE_SCHEMA.`

const TRANSFER_PROMPT = `${COMMON}

Lane: OI-04 — wire parliamentary_transfer.propose_transfer (territory one-way ratchet). The
preflight verified: it needs a THIRD parliamentary motion path (parliamentary_bridge's
run_parliamentary_scene composes only a domain echo; propose_censure is the Sanction sibling);
the only auto-populated CB is crown_constitutional_restoration (Crown <6 territories). Work:
1. In engine/cross_scale/parliamentary_bridge.py, add a transfer-motion derivation alongside the
   existing _derive_vote shape: when a qualifying CB exists (use _available_cb / the module's own
   CB machinery — NEVER invent or seed CB entries), derive (initiator, target_territory, mode)
   and route to systems/factions/sim/parliamentary_transfer.propose_transfer; otherwise the
   season proceeds exactly as today (no behavior change when no CB qualifies).
2. Choose the derivation minimally and cite canon for every choice (which territory, which mode)
   from parliamentary_transfer.py's own docstrings/§10 canon; where canon does not determine a
   choice, take the narrowest option and record it as [SEED] with the ED-SC-0006/0007 precedent.
3. Falsifier: a seeded engine/tests campaign (or focused test) in which Crown drops below 6
   territories, the auto-CB qualifies, propose_transfer runs, and on Success the territory list
   changes hands — assert the regain actually happened (assert checked >= 1). If no seed reaches
   it in bounded search, ship the wired path + a direct unit-level falsifier (call the derivation
   with a constructed world where the CB qualifies) and record the campaign-reachability gap
   honestly in notes.
4. golden_status: whether the new motion path consumes RNG or changes season flow in the CURRENT
   pinned campaigns (if the CB never qualifies in those seeds, the goldens must NOT move — verify
   and say so).
Return per LANE_SCHEMA.`

const HANDOFF_PROMPT = `${COMMON}

Lane: OI-06 — wire handoff_rules.py as the vertical-up dispatcher validity layer (import-orphan;
its 3 apparent importers are docstring mentions). Work:
1. In engine/cross_scale/scene_dispatch.py, consume handoff_rules.apply_handoff(from_scale,
   to_scale, payload, world) at the scale-transition point (alongside the zoom_in_out calls —
   read the current post-W1 shape first); a valid=True result proceeds exactly as today; the
   valid=False fallback (handoff_rules.py:226-232, 'No §3 rule defined') becomes a VISIBLE
   stubwire flag (reuse the existing OI-02 fallback pattern in the same file), never a silent
   dict.
2. scale pair derivation: only from fields dispatch already has; do not invent scales — keys.py
   SCALES is the only legal vocabulary.
3. §3.3 Personal→Contest stays an EMPTY heading (ED-IN-0049, §5 fork 11) — if a dispatch path
   hits it, that is a stubwire flag citing the fork, not new content.
4. Tests: the 8 built §3 rules exercised through dispatch (or directly where dispatch cannot
   reach them yet — record which); the invalid-pair path asserts the stubwire flag fires.
5. golden_status: the validity layer must be behavior-neutral for every currently-valid
   transition in the pinned campaigns — verify by running engine/tests locally and say so.
Return per LANE_SCHEMA.`

const ARTIC_PROMPT = `${COMMON}

Lane: OI-08 — the articulation minimal subscriber (kills the zero-subscriber state; renders
nothing). Preflight facts: TickScheduler.subscribe (engine/substrate/keys.py:447) has ZERO
callers anywhere — articulation will be the first; the §3.1 trigger table
(systems/articulation/articulation_layer_v30.md:77-92) lists 10 type_ids (state.scar_acquired,
state.coup_attempted, state.succession, mechanical.mission_shift, da.covert_betrayal,
meta.knot_formed, meta.knot_ruptured, env.peninsular_strain_shock, meta.cascade_cluster_event,
state.belief_revised). NOTE meta.cascade_cluster_event is UNREGISTERED in the key-type registry
(OI-27b, §5 fork 11) — subscribe to the other 9 and record the 10th as held-on-fork (do NOT
register new key types; that is Wave 3/J territory). Work:
1. engine/cross_scale/articulation.py: a subscribe_all(scheduler) entry point registering a
   callback per type_id; each callback is a per-invocation stubwire flag (module='…articulation',
   reason cites ED-IN-0073's docket for the render layer) that stores nothing and renders nothing.
2. Wire subscribe_all at scheduler creation (find where the TickScheduler/echo_scheduler is
   constructed in engine/mc_v18.py — COORDINATE: mc_v18.py is the World lane's file; put the
   one-line hook spec into oracle_requests/notes as 'mc_v18 hook needed: <exact line + call>' and
   implement everything callable-side yourself; if a non-mc_v18 construction site exists (e.g.
   scheduler factory in keys.py consumers), prefer it).
3. Tests: tests/valoria/test_articulation_subscriber.py — subscribe_all registers >= 9 types
   (assert counted); an emitted Key of a subscribed type increments the stubwire invocation
   counter (end-to-end through TickScheduler).
4. golden_status: subscription alone must not move any golden (callbacks are no-ops; verify no
   pinned key_log_hash-style pin counts subscriptions).
Return per LANE_SCHEMA.`

const CENSUS_PROMPT = `${COMMON}

Lane: OI-12 census (verify-before-wiring; effort low). The preflight verified: 7 of the OI-12
modules were already stub-wired in W1 (npc_ai, companion, rs_track, ip_track, rendering,
miraculous_event, restoration_movement) — nothing to do but record; 7 are REAL implemented code
with zero importers and NO doc-specified call site (co_movement, collective, opposing,
settlement, temperaments, parliamentary_stay, engine.autoload.registry). Work — documentation
only (no code edits):
1. Re-verify each of the 14 in the current tree (import-orphan status, stub-wired vs real).
2. For the 7 real-code orphans: grep each module's own docstring canon-source line + its
   subsystem design head for a specified call site; the preflight found none — confirm or refute
   per module with evidence.
3. Write the census into audit/2026-07-29-code-shape-open-items/04_execution_ledger.md as OI-12
   rows: per module — already-stub-wired(W1) | wired-this-wave-by-<lane> (settlement/temperaments
   may be consumed by the World lane — check its files_touched at bookkeeping time, mark
   provisional here) | verified-orphan-no-specified-callsite (honest recorded miss, W5 census
   input). NO module gets force-wired or stub-converted (they are real code).
4. oracle_requests: none expected; note if any census finding invalidates an existing manifest row.
Return per LANE_SCHEMA.`

const [echoL, transferL, handoffL, articL, censusL] = await parallel([
  () => agent(ECHO_PROMPT, { schema: LANE_SCHEMA, label: 'seam:accord-echo', phase: 'Seams', model: 'sonnet', effort: 'high' }),
  () => agent(TRANSFER_PROMPT, { schema: LANE_SCHEMA, label: 'seam:territory-transfer', phase: 'Seams', model: 'sonnet', effort: 'high' }),
  () => agent(HANDOFF_PROMPT, { schema: LANE_SCHEMA, label: 'seam:vertical-handoff', phase: 'Seams', model: 'sonnet', effort: 'high' }),
  () => agent(ARTIC_PROMPT, { schema: LANE_SCHEMA, label: 'seam:articulation-subscriber', phase: 'Seams', model: 'sonnet', effort: 'high' }),
  () => agent(CENSUS_PROMPT, { schema: LANE_SCHEMA, label: 'seam:oi12-census', phase: 'Seams', model: 'sonnet', effort: 'low' }),
])

run.lens('seam:accord-echo', echoL ? [echoL] : [])
run.lens('seam:territory-transfer', transferL ? [transferL] : [])
run.lens('seam:vertical-handoff', handoffL ? [handoffL] : [])
run.lens('seam:articulation-subscriber', articL ? [articL] : [])
run.lens('seam:oi12-census', censusL ? [censusL] : [])

phase('World')

const WORLD_PROMPT = `${COMMON}

Lane: OI-05 + OI-07 — the world-population lane, and THE declared IN-family golden re-record.
You are the SOLE writer of engine/mc_v18.py and engine/autoload/game_state.py this wave. The
seam lanes have landed; their notes may request one-line mc_v18 hooks:
ARTICULATION LANE OUTPUT: ${JSON.stringify(articL)}
(implement any 'mc_v18 hook needed' request from it verbatim).
Work:
1. OI-05: wire systems/world/sim/npe.py — generate_npc at world-gen (initial population per the
   NPE design head's own numbers — cite them; if the head does not specify an initial count,
   generate none at world-gen and only via the season path that IS specified) and
   simulate_npc_actions in the season loop at the Accounting-adjacent point the design head names.
   Every count/parameter cites its canon; nothing invented.
2. OI-07: populate world.settlements at world-gen via systems/settlements/sim/registry.py's
   register_settlement from the canonical geography source (find it — the PP-726-rebuilt
   geography YAML; cite it); add the missing 'settlements' serialization keys in game_state.py
   (mirror the npcs/knots pattern at :273-365). world.knots: wire form_knot ONLY per a canonical
   formation rule from the knots design head — if no world-gen/season formation rule exists in
   canon, populate nothing, route the formation trigger through a stubwire flag citing the gap,
   and record it (honest deferral beats invented knots).
3. THE GOLDEN RE-RECORD (declared): any new RNG draw shifts every downstream pin. Re-record
   deliberately: run each campaign-golden test, capture old vs new for EVERY moved pin in
   engine/tests/{test_f7_smoke_oracle,test_mc_v18_regression,test_echo_transport,
   test_parliamentary_bridge}.py; preserve old values in comments citing OI-05/ED-IN-0095; the
   npcs==0 assertion flips to a positive pinned count. Produce the full before/after table in
   your notes (the PR body carries it). Consider gating world-population behind a default-ON
   named constant ONLY if canon demands configurability — otherwise wire directly; no
   double-bookkeeping flags without canon.
4. Falsifiers: an NPE season over the populated store asserting >= 1 npc action
   (assert checked >= 1); settlements count == the geography source's count (assert exact);
   serialization round-trip for settlements.
5. oracle_requests: which manifest rows are now flippable (world-npcs, world-knots [or its
   honest-deferral reshaping], world-settlements).
Return per LANE_SCHEMA (golden_status = the full moved-pin list).`

const worldL = await agent(WORLD_PROMPT, { schema: LANE_SCHEMA, label: 'world:population+goldens', phase: 'World', model: 'sonnet', effort: 'high' })
run.lens('world:population+goldens', worldL ? [worldL] : [])

phase('Oracle')

const ORACLE_PROMPT = `${COMMON}

Lane: the SOLE editor of engine/tests/test_pipeline_reach.py this wave. Inputs — every lane's
oracle_requests:
${JSON.stringify([echoL, transferL, handoffL, articL, censusL, worldL].map(l => l && { lane: l.files_touched && l.files_touched[0], requests: l.oracle_requests, notes_excerpt: (l.notes || '').slice(0, 400) }))}
Work: for each W2 manifest row (accord-echo-leg, vertical-up-handoff, territory-transfer-resolver,
world-npcs, world-knots, world-settlements): flip to strict ONLY where the wiring landed and the
strict assertion passes against the tree (run the test); where a lane recorded an honest deferral
(e.g. knots formation rule gap), REWRITE the row's reason to cite the new state (stub-flagged with
its gap named) rather than leaving a stale reason. Add NEW rows/assertions the wave created a
basis for: articulation subscriber (>= 9 subscribed types, stub-flag invocations visible),
OI-12's verified-orphan census pointer (a manifest row per still-orphan module is overkill — one
census row citing the execution ledger is enough). Never assert a Key scale outside keys.py
SCALES. Run the full file + the golden files after edits; report tails in notes.
Return per LANE_SCHEMA.`

const oracleL = await agent(ORACLE_PROMPT, { schema: LANE_SCHEMA, label: 'oracle:manifest-flips', phase: 'Oracle', model: 'sonnet', effort: 'high' })
run.lens('oracle:manifest-flips', oracleL ? [oracleL] : [])

phase('Adjudicate')

const adj = await agent(`${COMMON}

Opus adjudication of Wave 2's three judgment-heavy seams (module-adjudicator method; read-only —
name fixes, do not make them):
1. ECHO SEMANTICS: the new outcome-classification + compute_accord_echo call — is every §5.5
   mapping row faithful to scale_transitions_v30.md §5.5 (read it)? Does any classification
   invent an outcome canon does not back? Is the Accord write applied to the RIGHT territory?
2. TRANSFER PATH: is the CB gating honest (no invented CB sources)? Is the (initiator, territory,
   mode) derivation canon-cited or properly [SEED]-marked? Does the no-CB season remain
   byte-identical?
3. WORLD POPULATION: are the NPC counts/points canon-cited? Is the settlements population sourced
   from the canonical geography file with an exact-count assertion? Is the knots decision (wire vs
   honest deferral) correct against the knots head? Is the golden re-record COMPLETE (no moved pin
   left unrecorded — run the suites and compare against the lane's before/after table)?
LANE OUTPUTS:
ECHO: ${JSON.stringify(echoL)}
TRANSFER: ${JSON.stringify(transferL)}
WORLD: ${JSON.stringify(worldL)}`,
  { schema: ADJ_SCHEMA, label: 'adjudicate:w2', phase: 'Adjudicate', model: 'opus', effort: 'high' })
run.lens('adjudicate:w2', adj && adj.closure_findings ? adj.closure_findings : [])

phase('Critic')

const critic = await run.attempt('critic:w2',
  agent(`Adversarial critic relay for Wave 2 of the code-shape program (repo /home/user/ttrpg;
judge from file contents — the wave's changes are uncommitted/committed in the working tree). You
receive producers' OUTPUT only. Try to BREAK the wave against 01_orchestration_plan_v1.md §3
Wave 2's exit criteria + §0.1:
1. SEAM STOPS: any touch of systems/combat/**, wrapper.py, faction_action.py,
   id_reservations.yaml, review_baseline.yaml in the diff?
2. GOLDEN HONESTY: is the re-record COMPLETE and LOUD — every moved pin captured with old value
   preserved, none silently re-recorded, none missed (run-compare if you can read test outputs in
   notes; otherwise verify the table covers every pinned constant in the four golden files)?
3. FABRICATION HUNT: any invented NPC counts, CB sources, knot formation rules, or §5.5 outcome
   mappings without canon citations? Check each numeric constant's provenance line.
4. ORACLE HONESTY: every flipped row genuinely strict (assertions can fail)? Every rewritten
   xfail reason accurate? assert-that-asserted present on conditional loops?
5. DEFERRALS: is the knots decision (if deferred) and the census's no-specified-callsite list
   honest — or did anything get quietly force-wired?
6. What is MISSING that the exit criteria require (reach-oracle direction rows strict; orphan
   count measurably down with delta recorded)?
Finding nothing is a real verdict.
PRODUCER OUTPUT:
${JSON.stringify({ echoL, transferL, handoffL, articL, censusL, worldL, oracleL, adj })}`,
    hCritic({ schema: CRITIC_SCHEMA, label: 'critic:w2', phase: 'Critic', model: 'opus', effort: 'high' })))

// ARITY, not just the method name. The owner's signature is
// `run.critiqued(stage, produced, reviewed)`; this call passed a single ARRAY, so
// `produced` was undefined, `undefined > 0` was false, and the critic-starvation signal
// could never fire from here. Same copy-paste lineage as the dispute defect eight lines
// below, and it survived that fix because the gate checked names and not shapes.
const CRITIQUED_STAGES = ['seam:accord-echo', 'seam:territory-transfer', 'seam:vertical-handoff', 'seam:articulation-subscriber', 'seam:oi12-census', 'world:population+goldens', 'oracle:manifest-flips']
run.critiqued('Critic', CRITIQUED_STAGES.length,
  (critic && critic.verdicts) ? CRITIQUED_STAGES.length : 0)
run.lens('critic:w2', critic && critic.verdicts ? critic.verdicts : [])

const overturns = (critic && critic.verdicts ? critic.verdicts : []).filter(v => v.verdict !== 'uphold')
for (const v of overturns) {
  // Built by the owner, not by hand: the four keys this call used to pass ({layer,target,
  // detail,severity}) are none of them keys run.dispute() reads, so every dispute this
  // script ever recorded was keyed '?' and could not be adjudicated. See hVerdictDispute.
  run.dispute(hVerdictDispute(v, 'critic:w2', v.target))
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

Bookkeeping for Wave 2, AFTER the critic (the orchestrator adjudicates disputes before commit —
your rows describe what landed, not what is still disputed; mark disputed items 'pending
orchestrator adjudication'). Edit ONLY: audit/2026-07-29-code-shape-open-items/04_execution_ledger.md,
registers/editorial_ledger_in.jsonl + registers/editorial_ledger_{fa,wr,se}.jsonl,
registers/handoffs/HANDOFF_IN.md, root HANDOFF.md. NEVER other lanes' handoff files (F12 — the
cross-lane EDs are visible to those sessions via their lane LEDGER files + the PR body).
1. Allocate from the W0a-reserved blocks (id_reservations.yaml is FROZEN — record assignments in
   the ledgers + execution ledger only): ED-IN-0095 (W2 umbrella: seams + oracle + census),
   ED-FA-0036 (OI-04 transfer motion path), ED-WR-0009 (OI-05 NPC generation + NPE season wiring
   + the golden re-record), ED-SE-0049 (OI-07 settlements population + serialization). Schema-copy
   each lane file's latest entries; each entry cites ED-IN-0091 parent + its OI row(s).
2. Execution-ledger rows per wave item (OI-03/04/05/06/07/08/12), each with falsifier + outcome;
   include the G12 corrections (LPS-2e→§5.5 citation; the knots/census honest deferrals if any).
3. HANDOFF_IN: program entry updated (W2 landed, contents, next = W3 Keys/contract truth). Root
   HANDOFF: program line updated.
Validate every JSONL file parses after editing. Return per LANE_SCHEMA (falsifier = the ED ids
allocated + where recorded).`,
  { schema: LANE_SCHEMA, label: 'bookkeeping', phase: 'Bookkeeping', model: 'sonnet', effort: 'low' })
run.lens('bookkeeping', book ? [book] : [])

return {
  run: run.summary(),
  echoL, transferL, handoffL, articL, censusL, worldL, oracleL, adj, critic, ranked, book,
  orchestrator_note: 'Gate: adjudicate disputes -> fix batch if needed -> re-critic if fixes are substantive -> full suites + validators -> commit/PR/merge with the golden before/after table in the body.',
}
