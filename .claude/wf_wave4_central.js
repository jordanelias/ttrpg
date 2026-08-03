export const meta = {
  name: 'wave4-central',
  description: 'W4 of the code-shape program (ED-IN-0091/ED-IN-0097): centralization P2 — cycle break, dead-root sweep + guard extension, contract↔code join, __main__-guard single owner, mechanical retirements/index sweep',
  phases: [
    { title: 'Build', detail: '3 parallel file-disjoint lanes: cycle+dedup · dead-roots+guard · contract-code join', model: 'sonnet' },
    { title: 'Sweep', detail: 'mechanical bucket: OI-15/16 retirements, OI-51 verified-stale record, OI-57 indexing, OI-32a dead slice', model: 'sonnet (effort low)' },
    { title: 'Adjudicate', detail: 'dedup mutation checks + retirement evidence + join verification', model: 'opus' },
    { title: 'Critic', detail: 'read-only adversarial relay over the wave diff', model: 'opus' },
    { title: 'Bookkeeping', detail: 'ED-IN-0097 + execution ledger + HANDOFF_IN', model: 'sonnet (effort low)' },
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
// W4 executes 01_orchestration_plan_v1.md §3 Wave 4, as re-scoped by the 2026-07-29 G12 preflight
// (in-tree-verified; OVERRIDES the plan where they conflict):
// - OI-51 IS ENTIRELY STALE: ED-871/ED-912/fork-2/fork-11-propagation/conviction_track all
//   EXECUTED pre-program (traced to commit f60b74d, PR #203; tests exist and pass). The sweep
//   records verified-stale, executes NOTHING for it.
// - OI-52a: both cycle edges are already lazy (game_state.py:370 / npe.py:184) — graph-hygiene
//   break only; npe.py:184's `canonical_accord` reach-back is the smaller direction.
// - OI-53a: 4 live dead-root sites confirmed (audit_staleness.py:69, build_decisions.py:57,
//   workplan_status.py:71, ci_audit_registry_check.py:23) + build_apparatus_registry.py:232/:234
//   globs the deleted designs/audit tree. Route through ci_common (single owner); EXTEND
//   tests/valoria/test_retired_tree_apparatus.py; never a second owner/guard.
// - OI-54: mechanics_index.yaml already carries sim_module: on 88 entries — the join leverages
//   it; module_contracts.yaml gets sim_module: 27/27 (explicit `none` + reason for the 9
//   doc:null/no-sim modules), structure_audit upgraded name-match → join-verified (declared
//   paths must resolve as real G_code nodes), report-only review_core signal.
// - __main__-guard single owner: move the AST predicate to tools/ci_common.py; both
//   build_apparatus_registry.py (plain import) and structure_audit.py (sys.path idiom, precedent
//   in test_retired_tree_apparatus.py) consume it. Mutation check: perturb the owner, both fail.
// - OI-15: the 4 orphaned tools have re-verified zero invokers (ED-1082 grep precedent) —
//   retire to deprecated/tools/ + fix apparatus_registry's harness.py contradictory triple.
// - OI-16: tools/registry.py facade has zero production consumers — retire to deprecated/tools/
//   (with its unit test); head_pointers.yaml + REPO_MAP.md recorded NOT-TO-BE-BUILT (the
//   PROPOSALS family + CURRENT.md already serve the converged-pointer role) — ledger row.
// - OI-57: index franchise_v30 + faction_succession_split_v30 in registers/mechanics_index.yaml
//   (insurgency_pipeline claim is STALE — already indexed; record). CURRENT.md rows are
//   FA-owned — NOT added here (single-writer table); courtesy-flagged in the PR body. ED-1054:
//   close its loop honestly (2 targets point at the deleted sim/ tree; tools/README.md half done).
// - OI-32a dead slice: mc_v18.py:44's dead VICTORY_THRESHOLD:11 param copy + game_state.py:101
//   intel field — the F7 dead-param TRIPWIRE test must stay meaningful (it exists to trip when
//   the param wires to a live gate): document/annotate rather than delete where deletion would
//   kill the tripwire's subject; the intel field may be removed only if serialization and no
//   test reference it (verify).
// - vocab.a17: current 21 vs baseline 29 — 8 rows of BANKED SHRINK; do NOT edit the baseline
//   (CODEOWNERS/Jordan); the wave STOPS only if its own edits push the count ABOVE 29.
// - NO golden may move. Seam stops unchanged (systems/combat/**, wrapper.py, faction_action.py,
//   id_reservations.yaml, review_baseline.yaml). Oracle file: no W4 rows exist; do not edit it.
// - File ownership: L-cycle -> engine/autoload/game_state.py + systems/world/sim/npe.py +
//   tools/ci_common.py + tools/build_apparatus_registry.py + skills/valoria-vector-audit/scripts/structure_audit.py
//   (predicate + join upgrade share structure_audit — L-cycle owns ci_common+apparatus,
//   L-join owns structure_audit + module_contracts + review_core; the predicate import in
//   structure_audit is L-join's edit per L-cycle's ci_common function name, coordinated via
//   the pinned name below); L-roots -> the 4 dead-root tools + test_retired_tree_apparatus.py;
//   SWEEP -> deprecated/tools/ moves + apparatus_registry regen? NO — the apparatus registry is
//   a GENERATED artifact; IN is sole regenerator AT WAVE 5 (single-writer table). The sweep
//   edits sources only and notes regeneration deferred to W5.
// - PINNED NAME: the shared predicate lands as ci_common.has_main_guard(tree) (AST-based, both
//   operand orders — the stricter of the two current implementations).
// ---------------------------------------------------------------------------------------------

const run = hRun('wave4-central')

const LANE_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['files_touched', 'tests_added', 'falsifier', 'golden_status', 'stopped_items', 'notes'],
  properties: {
    files_touched: { type: 'array', items: { type: 'string' } },
    tests_added: { type: 'array', items: { type: 'string' } },
    falsifier: { type: 'string' },
    golden_status: { type: 'string' },
    stopped_items: { type: 'array', items: { type: 'string' } },
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
audit/2026-07-29-code-shape-open-items/01_orchestration_plan_v1.md §3 Wave 4 + this script's
header corrections (in-tree-verified; they OVERRIDE the plan) + 00_open_items_register.md for
your OI rows. Claims are LEADS — re-verify at cited file:line before acting. Every dedup ships
its equality/mutation test; every retirement follows the ED-1082 precedent (grep every
workflow/hook/skill for the filename BEFORE moving, record the greps). NO golden may move; if
one would, STOP the item. STOP-list: systems/combat/**, wrapper.py, faction_action.py:349,
id_reservations.yaml, review_baseline.yaml, engine/tests/test_pipeline_reach.py. Return per
LANE_SCHEMA.`

phase('Build')

const CYCLE_PROMPT = `${COMMON}

Lane: OI-52a cycle break + the __main__-guard single owner (W0b handoff).
1. Break engine.autoload.game_state ↔ systems.world.sim.npe: both edges are lazy (graph hygiene,
   not runtime). Smaller direction: npe.py:184's function-local
   'from engine.autoload.game_state import canonical_accord'. Options in order of preference:
   (a) if canonical_accord is a small pure function, relocate it to a no-deps home BOTH can
   import at top level (engine/substrate/ or a tiny shared module — check what canonical_accord
   actually does and where it canonically belongs; cite); (b) invert so game_state passes the
   needed value into npe's call. Verify post-fix: structure_audit reports 3 cycles (this one
   gone; contest + 2 MB cycles remain — do not touch them).
2. ci_common.has_main_guard(tree): move structure_audit.py's AST predicate (the stricter one —
   both operand orders) into tools/ci_common.py under the PINNED name; build_apparatus_registry.py
   imports it directly (same dir) replacing its regex at :116; leave a coordination note in your
   notes for the join lane (which owns structure_audit.py this wave) stating the exact import
   idiom to adopt (the sys.path precedent in tests/valoria/test_retired_tree_apparatus.py).
   ALSO fix build_apparatus_registry.py:232/:234's deleted-tree glob (designs/audit) — repoint at
   the live g_code.json home (find where structure_audit --output-dir runs actually write; if no
   stable live home exists, make the fallback an EXPLICIT no-op with a comment, never a silent
   empty glob).
3. Tests: cycle-gone assertion (structure_audit output); has_main_guard known-answer (conventional
   + reversed + string/comment false-positive rejection) in tests/valoria/ + the mutation check
   documented (perturb the owner, both consumers fail).
Return per LANE_SCHEMA.`

const ROOTS_PROMPT = `${COMMON}

Lane: OI-53a dead-root sweep (re-verified sites). Fix the four live dead-root references by
routing each through the EXISTING single owner ci_common.sim_reference_roots() (or, where the
need is prefix-lists for changed-file filtering rather than sim roots, a sibling ci_common
function — read what each site actually needs; if a new sibling is required, ONE function, in
ci_common, with the same live-glob discipline):
- tools/audit_staleness.py:69 (scope_prefixes tuple carries retired 'designs/', 'sim/')
- tools/observability/build_decisions.py:57 (SWEEP_DIRS carries 'designs', 'sim')
- tools/workplan_status.py:71 (RELEVANT_PREFIXES carries 'designs/', 'sim/')
- tools/ci_audit_registry_check.py:23 (AUDIT_DIR = designs/audit — the live home is audit/)
Each fix: re-verify the site at execution (a fifth may have landed; a listed one may be fixed),
expected-delta honesty (does the tool's output change when the dead prefixes drop? record it —
e.g. audit_staleness's in-scope counts may shift; that is a REPORTED delta, not a silent one).
EXTEND tests/valoria/test_retired_tree_apparatus.py: add designs/ + designs/audit/ to its scan
set so a planted regression in ANY of the four fixed files (and build_apparatus_registry.py)
fails the guard. Never a second owner or second guard file (§8).
Return per LANE_SCHEMA (golden_status: these are tools — verify no pytest golden reads their
output; audit_staleness feeds the SessionStart banner only).`

const JOIN_PROMPT = `${COMMON}

Lane: OI-54 contract↔code join. You own references/module_contracts.yaml,
skills/valoria-vector-audit/scripts/structure_audit.py, and tools/review_core.py this wave.
1. module_contracts.yaml: add sim_module: to all 27 modules — a repo-relative path (verify each
   resolves to a real file AND a real G_code node) or 'none' + a reason comment (the 9
   doc:null/no-sim modules per the preflight: npc_memory, scene_slate, game_director, scene_timer,
   audit, domain_actions, settlement_economy, engine_clock, scenario_authoring — plus any
   doc-only module like victory/articulation_layer where the code home is differently-named:
   articulation_layer -> engine/cross_scale/articulation.py is a legitimate explicit path even
   though it is not under systems/*/sim). Cross-check against registers/mechanics_index.yaml's
   existing 88 sim_module: entries (cite where used; discrepancies recorded, not papered).
2. structure_audit.py: upgrade l2_contract_without_code() from name-segment match to
   JOIN-VERIFIED — read the contracts' sim_module: fields, resolve each declared path to a
   G_code node, report joined/none/unresolvable counts; the scorecard line drops UNVERIFIED.
   Also adopt ci_common.has_main_guard via the sys.path idiom per the cycle lane's coordination
   note (their notes name the function; test_retired_tree_apparatus.py shows the idiom),
   deleting the local predicate.
3. review_core.py: add a report-only 'contracts.join' CHECKS row (count_re = unresolvable
   count; a CLI mode on structure_audit or a small flag that prints it) + the baseline entry —
   ONLY if review_baseline.yaml edits are permitted... they are NOT (frozen this wave, no
   pre-declared protocol). So: add the CHECKS row with NO baseline entry (review_core tolerates
   a missing baseline row as ceiling-0/absent? READ _apply_ratchet first: if a missing baseline
   entry makes a failing signal regress, DEFER the CHECKS row to W5 with a ledger note instead —
   never touch review_baseline.yaml).
4. Falsifier: a fictional contract entry with a bogus sim_module: must be reported unresolvable
   (fixture test); the join count is exact (assert == 27 rows accounted).
Return per LANE_SCHEMA.`

const [cycleL, rootsL, joinL] = await parallel([
  () => agent(CYCLE_PROMPT, { schema: LANE_SCHEMA, label: 'build:cycle+dedup', phase: 'Build', model: 'sonnet', effort: 'high' }),
  () => agent(ROOTS_PROMPT, { schema: LANE_SCHEMA, label: 'build:dead-roots', phase: 'Build', model: 'sonnet', effort: 'high' }),
  () => agent(JOIN_PROMPT, { schema: LANE_SCHEMA, label: 'build:contract-join', phase: 'Build', model: 'sonnet', effort: 'high' }),
])

run.lens('build:cycle+dedup', cycleL ? [cycleL] : [])
run.lens('build:dead-roots', rootsL ? [rootsL] : [])
run.lens('build:contract-join', joinL ? [joinL] : [])

phase('Sweep')

const SWEEP_PROMPT = `${COMMON}

Lane: the mechanical sweep bucket (OI-15/16/51/57/32a), effort low, documentation-heavy.
1. OI-15 retirements (ED-1082 precedent — re-run the greps yourself, record them): move
   tools/build_audit_registry_backfill.py, tools/geography/jsx_to_canonical.py,
   tools/measure_stamp_false_positives.py, tools/observability/npc_audit_report_gen.py to
   deprecated/tools/ (git mv equivalents via plain mv; note deprecated/tools/README.md if one
   exists — append entries). Do NOT regenerate references/apparatus_registry.yaml (IN regenerates
   at W5, single-writer table) — but DO fix the harness.py contradictory triple at its SOURCE if
   the flag is computed by build_apparatus_registry.py (read how orphaned: is derived; if the
   contradiction is generator logic, fix the generator; if it is stale generated data, record
   for the W5 regen).
2. OI-16: retire tools/registry.py + tests/valoria/test_registry.py to deprecated/tools/ (zero
   production consumers, re-verified); ledger row records head_pointers.yaml + REPO_MAP.md as
   NOT-TO-BE-BUILT with the rationale (PROPOSALS family + CURRENT.md serve the role).
3. OI-51: VERIFIED-STALE record only — write the ledger row citing the preflight evidence
   (ED-871/ED-912/fork-2/fork-11-propagation/conviction_track all executed pre-program, commit
   f60b74d; tests pass). Execute NOTHING.
4. OI-57: add mechanics_index.yaml entries for franchise_v30 + faction_succession_split_v30
   (schema-copy existing entries; sim_module: none where no sim exists; cite the docs).
   Record insurgency_pipeline's claim STALE (already indexed :859-867). ED-1054: update its
   HANDOFF_IN open-item text honestly (2 targets point at the deleted sim/ tree — moot;
   tools/README.md half done — verified) and mark the ED's disposition in the ledger row.
   CURRENT.md rows for the FA docs: NOT added (FA-owned; courtesy-flag in notes for the PR body).
5. OI-32a dead slice: mc_v18.py:44's VICTORY_THRESHOLD:11 dead param copy — annotate it as the
   F7 tripwire's subject (the test exists to trip when it wires; deleting it kills the tripwire —
   add the comment linking both). game_state.py:101 intel field: verify no serialization/test
   reads it; if truly free, remove it + its comment; if anything references it, annotate-only
   and record.
Return per LANE_SCHEMA.`

const sweepL = await agent(SWEEP_PROMPT, { schema: LANE_SCHEMA, label: 'sweep:mechanical', phase: 'Sweep', model: 'sonnet', effort: 'low' })
run.lens('sweep:mechanical', sweepL ? [sweepL] : [])

phase('Adjudicate')

const adj = await agent(`${COMMON}

Opus adjudication (read-only; name fixes, don't make them):
1. DEDUP MUTATION CHECKS: for has_main_guard — perturb-the-owner reasoning: would both consumers
   (build_apparatus_registry import + structure_audit sys.path import) genuinely fail on an owner
   change? Is the old regex fully gone (no second definition anywhere)?
2. CYCLE: is the break real (run/read structure_audit output: 3 cycles, the right three)? Did the
   relocation of canonical_accord (or chosen mechanism) preserve exact behavior (callers, values)?
3. JOIN: 27/27 accounted with honest none-reasons? Do all declared paths resolve to real G_code
   nodes? Is the fictional-contract fixture falsifier real? Was review_baseline.yaml touched
   (STOP-condition if so)?
4. DEAD ROOTS: each fix routed through ci_common (no second owner)? Guard extended and would it
   fail on a planted regression in each scan root? Expected deltas REPORTED (audit_staleness
   counts etc.)?
5. RETIREMENTS: grep evidence recorded per file? Nothing retired that anything still invokes?
6. NO-GOLDEN: any pinned value at risk from the intel-field removal / retirements?
LANE OUTPUTS: ${JSON.stringify({ cycleL, rootsL, joinL, sweepL })}`,
  { schema: ADJ_SCHEMA, label: 'adjudicate:w4', phase: 'Adjudicate', model: 'opus', effort: 'high' })
run.lens('adjudicate:w4', adj && adj.closure_findings ? adj.closure_findings : [])

phase('Critic')

const critic = await run.attempt('critic:w4',
  agent(`Adversarial critic relay for Wave 4 (repo /home/user/ttrpg; judge from file contents).
Producers' OUTPUT only. Break the wave vs 01_orchestration_plan_v1.md §3 Wave 4's exit + §0.1 +
the header re-scopes:
1. Single-owner honesty: is has_main_guard truly single-owned now (corpus grep)? Any dedup
   without its mutation/equality test?
2. Retirement safety: re-grep the four retired tools + registry.py across workflows/hooks/skills/
   imports yourself — anything the sweep's greps missed?
3. Join truth: spot-check 6 sim_module: declarations against the tree (do the paths exist and
   match the module's real code home?); the 'none' reasons against the doc:null realities.
4. Dead-root guard: would test_retired_tree_apparatus.py actually fail on a planted 'designs/'
   reference in EACH of the five fixed files?
5. vocab.a17 + goldens: did anything move the a17 count above 29 or any pinned golden?
6. OI-51 verified-stale record: is the evidence chain (f60b74d, passing tests) accurately cited?
7. MISSING vs exit criteria: review_core --check no regression; every dedup's test present;
   the banked a17 shrink flagged (not silently absorbed); ED-1054 loop honestly closed.
Finding nothing is a real verdict.
PRODUCER OUTPUT: ${JSON.stringify({ cycleL, rootsL, joinL, sweepL, adj })}`,
    hCritic({ schema: CRITIC_SCHEMA, label: 'critic:w4', phase: 'Critic', model: 'opus', effort: 'high' })))

// ARITY, not just the method name. The owner's signature is
// `run.critiqued(stage, produced, reviewed)`; this call passed a single ARRAY, so
// `produced` was undefined, `undefined > 0` was false, and the critic-starvation signal
// could never fire from here. Same copy-paste lineage as the dispute defect eight lines
// below, and it survived that fix because the gate checked names and not shapes.
const CRITIQUED_STAGES = ['build:cycle+dedup', 'build:dead-roots', 'build:contract-join', 'sweep:mechanical']
run.critiqued('Critic', CRITIQUED_STAGES.length,
  (critic && critic.verdicts) ? CRITIQUED_STAGES.length : 0)
run.lens('critic:w4', critic && critic.verdicts ? critic.verdicts : [])

const overturns = (critic && critic.verdicts ? critic.verdicts : []).filter(v => v.verdict !== 'uphold')
for (const v of overturns) {
  // Built by the owner, not by hand: the four keys this call used to pass ({layer,target,
  // detail,severity}) are none of them keys run.dispute() reads, so every dispute this
  // script ever recorded was keyed '?' and could not be adjudicated. See hVerdictDispute.
  run.dispute(hVerdictDispute(v, 'critic:w4', v.target))
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

Bookkeeping for Wave 4, AFTER the critic (disputes are the orchestrator's). Edit ONLY the
execution ledger, registers/editorial_ledger_in.jsonl, registers/handoffs/HANDOFF_IN.md, root
HANDOFF.md. Allocate ED-IN-0097 (W4 umbrella) from the reserved block (id_reservations FROZEN).
Rows: OI-52a (cycle broken, 4→3), the __main__-guard single owner (closes the W0b routed row —
flip its status), OI-53a (4 sites + apparatus glob fixed, guard extended, deltas reported; closes
the W0b routed row), OI-54 (27/27 join + upgraded check; review_core row deferred-or-added per
what the join lane did), OI-15 (4 retirements + harness.py fix/record; apparatus regen deferred
to W5), OI-16 (facade retired; pointer artifacts NOT-TO-BE-BUILT with rationale), OI-51
(VERIFIED-STALE, no-op, evidence cited), OI-57 (2 indexed; insurgency claim stale; ED-1054 loop
closed; FA CURRENT.md rows courtesy-flagged), OI-32a (tripwire annotated; intel field per what
landed), the banked a17 shrink 29→21 (DECISION ITEM for Jordan: baseline-lowering ED,
CODEOWNERS). MEASURED-BY lines on any quantitative claim (claim-provenance gate). HANDOFF_IN:
W4 landed, next = W5 capstone. Validate JSONL + register sizes (archive uncited resolved entries
per the established procedure if over cap). Return per LANE_SCHEMA.`,
  { schema: LANE_SCHEMA, label: 'bookkeeping', phase: 'Bookkeeping', model: 'sonnet', effort: 'low' })
run.lens('bookkeeping', book ? [book] : [])

return {
  run: run.summary(),
  cycleL, rootsL, joinL, sweepL, adj, critic, ranked, book,
  orchestrator_note: 'Gate: adjudicate disputes -> fix batch if needed -> re-critic if substantive -> full suites + validators (no golden, a17 <= 29, review_baseline untouched) -> commit/PR/merge on CI green.',
}
