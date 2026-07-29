export const meta = {
  name: 'combat-system-critique',
  description: 'Intensive NERS + resolution + contract audit of personal-combat engine, corpus reconciliation, adversarial verify, distillation',
  phases: [
    { title: 'Module-NERS', detail: 'one agent per state-graph module cluster — NERS + IN/resolver/OUT contract + dead-data + churn' },
    { title: 'Resolution', detail: 'Instance-A rolling-engine property test (P-i..P-v) on core resolver + sub-resolvers' },
    { title: 'Reconcile', detail: 'one agent per uploaded corpus — curious extension + adversarial review of what improves the engine' },
    { title: 'Adversarial', detail: 'skeptics try to refute the top findings and NERS-vet every proposed addition' },
    { title: 'Distill', detail: 'synthesize the distillation proposal: cut / consolidate / minimal NERS-clean core' },
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

// P4 · the read-only critic. Independence is STRUCTURAL, not a sentence in a prompt: the
// agentType below is defined in .claude/agents/valoria-critic.md with a tools list that has no
// Write/Edit. Passing it is the whole mechanism — a critic stage that omits it can write, and
// tools/ci_wf_harness_check.py fails the script that does.
const H_CRITIC = { agentType: 'valoria-critic' }
function hCritic(opts) { return Object.assign({}, opts || {}, H_CRITIC) }
// ==== END VALORIA WF HARNESS v1 ====

const run = hRun('combat-system-critique')
// Paths are REPO-RELATIVE. They used to be absolute Windows paths off one author's machine
// (`C:/Github/ttrpg/...`, `C:/Users/Jordan/Downloads/...`), which resolve nowhere on CI, in a
// container, or on any other checkout — every agent in this workflow was reading nothing.
// Repaired ED-IN-0087; `tools/ci_claude_workflow_paths.py` is the guard that fails on recurrence.
const ENG = 'systems/combat/combat_engine_v1'
const SUBSTRATE = 'tests/sim/v32-combat-balance'
// The reconcile-phase corpora: recovered off Jordan's Downloads into the tree on 2026-06-29
// (see that dir's README.md — "where did the month of work go"). Reading them from Downloads was
// always a one-machine dependency; now they are versioned and every agent can actually open them.
const DL = 'audit/2026-06-29-combat-corpus-recovery'
const DELIB = 'audit/2026-06-28-social-contest-deliberation-critique/source-research'

const SHARED = `
You are auditing the Valoria PERSONAL-COMBAT engine. The WORKING TREE is the source of truth — read the actual files; do not trust any summary, doc, or memory over the code. Static analysis is the default; the engine IS importable if you need to check a value (see PORTABILITY below).

ENGINE DIR: ${ENG}/  (core.py, wrapper.py, combat_systems.py, combatant.py, weapons.py, config.py, tradition.py, traditions.py, geometry.py, contact.py, capabilities.py, state_graph.py, weapon_physics.py, ability_primitives.py, ability_armature.md, README.md, workbench/)
SIGMA SUBSTRATE: core.py resolves the sigma kernel through \`engine/autoload/sigma_leverage.py\` — the numpy-free single source, parity-tested at 1e-9 against the originals (engine/tests/test_sigma_leverage_parity.py).
FROZEN VALIDATION STATION: ${SUBSTRATE}/ (m1_dice_sigma_core.py = soft_cap/sigma_n/the net engine; r1_sigma_resolution.py = effective_ob/degree/resolution_pool; r8_parity_harness.py = roll wrappers/WoundTracker/stamina_max; damage_model.py). The engine NO LONGER IMPORTS THESE — read them as the canonical-constant reference the engine is parity-checked against, not as a live dependency.
CANON STATE MAP (audit companion, MAY BE STALE vs HEAD): audit/2026-06-09-personal-combat-comprehensive/combat_engine_flow_and_state_map.md

NERS: N — Necessary (no roll/lever/edge redundant; an ADDED mechanic must itself be necessary; lever-pile is the canonical defect). R — Robust (holds at extremes: leverage in-band, no cliffs, floors/caps respected, loops bounded = damper<1 AND cap, graded recoverable output, ER-2 continuity sub-5D). S — Smooth (transitions clean across scales/phases; consistent with sibling engines; no role-conflation at seams). E — Elegant (player intuits outcomes from legible odds; one number doing more work beats a new subsystem).
Personal combat is INSTANCE A (sigma-leverage continuous engine). Five properties: P-i legible odds; P-ii uniform/in-band leverage (σ_N-scaled, NOT flat +X); P-iii bounded+monotonic, no cliffs, Ob>=1 floor, ER-2 continuity; P-iv graded recoverable (not fragile binary, underdog floor); P-v right engine for the pool regime.
MODULE CONTRACT lens: every mechanic = IN(consumed) -> resolver -> OUT(emitted) + owned state. Flag dead-data (computed/stored, never consumed), orphan emissions, role-conflation (one variable, >1 job), undamped+unbounded loops.
CHURN PRINCIPLE: every mechanic must generate churn that seeds emergent narrative & meaningful choice. Suspect any inert/unreachable mechanic, any lever that only tunes but never branches the path, any choice with a dominant answer.

ALREADY-VERIFIED FACTS (confirm against code; extend; find MORE):
- core.resolve does a μ-SHIFT not Ob-shift: net = roll_net(pool) + m1.soft_cap(net_sigma)*m1.sigma_n(pool); boost IS σ_N-scaled (sigma_n=0.8*sqrt(pool)) so leverage is pool-uniform by construction; r1.effective_ob is display-only. soft_cap = 1.5*tanh(x/1.5) (M_MAX=1.5).
- ER-2 continuity correction is INLINE in core.degree() (thresholds read at k-0.5).
- mass/pob_frac NOW consumed by core.p_auth (blunt heft) — state map "F5 dead" is STALE. BUT armor_defeat_sigma still reads HAND-SET w['percussion'] for blunt armour-defeat → TWO competing percussion sources for one physical quantity.
- geometry.bake produces {gap,thrust,cut,perc_conc,halfsword}; only gap consumed; WEAPONS[w]['geo'] stored but never read → thrust/cut/perc_conc/halfsword are DEAD baked data.
- eff_cw IS wired at many sites now — state map "channels inert/pending" is STALE. precommit IS consumed (feint_eval def_read) — but only that one defender feint-resist site.
- 'seize' lever has NO consumer in wrapper.py/combat_systems.py (pre-contact seizure CUT 2026-06-05) → abilities 'vorschlag' AND 'sen_no_sen' (JAPANESE flagship) are DEAD; ability_armature.md still claims 'seize' is "live" → doc drift.
- 'clinch' weapon field — never consumed.
- PORTABILITY, RESOLVED — do NOT re-report it. The engine once reached into ${SUBSTRATE}/ for m1/r1/r8 via a sys.path hack on /home/claude & /home/claude/v32, which made it non-runnable off one sandbox and dragged numpy into the runtime. ED-1085 (2026-07-01) de-leaked it: sigma comes from engine/autoload/sigma_leverage.py, and the RNG contract changed with it (stdlib random.Random / rng.gauss, no longer a numpy Generator / rng.normal). Verify at core.py:13-20 before writing anything about imports. A NEW absolute or /home/claude path anywhere in the engine IS still a finding.

STYLE: curious in extension, adversarial in review (assume it's broken), judicious in reconciliation (credit what works; don't manufacture fault). Cite file:line for every claim. Severity P1 (breaks play/correctness), P2 (ambiguity/inert/drift), P3 (polish). Your output IS structured data.
`

const FINDING = {
  type: 'object', additionalProperties: false,
  required: ['id', 'severity', 'claim', 'evidence', 'kind'],
  properties: {
    id: { type: 'string' },
    severity: { type: 'string', enum: ['P1', 'P2', 'P3'] },
    kind: { type: 'string', enum: ['dead-data', 'orphan-emit', 'role-conflation', 'loop', 'cliff', 'leverage', 'redundancy', 'gap', 'doc-drift', 'churn-inert', 'correctness', 'portability', 'balance', 'other'] },
    claim: { type: 'string' },
    evidence: { type: 'string', description: 'file:line citations' },
  },
}
const CRIT = { type: 'object', additionalProperties: false, required: ['verdict', 'reason'], properties: { verdict: { type: 'string', enum: ['pass', 'fail', 'partial'] }, reason: { type: 'string' } } }
const NERS_BLOCK = { type: 'object', additionalProperties: false, required: ['N', 'R', 'S', 'E'], properties: { N: CRIT, R: CRIT, S: CRIT, E: CRIT } }
const MODULE_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['module', 'contract', 'ners', 'churn', 'findings', 'recommendations'],
  properties: {
    module: { type: 'string' },
    contract: { type: 'object', additionalProperties: false, required: ['consumes', 'emits', 'dead_data', 'orphans'], properties: { consumes: { type: 'array', items: { type: 'string' } }, emits: { type: 'array', items: { type: 'string' } }, dead_data: { type: 'array', items: { type: 'string' } }, orphans: { type: 'array', items: { type: 'string' } } } },
    ners: NERS_BLOCK,
    churn: { type: 'string' },
    findings: { type: 'array', items: FINDING },
    recommendations: { type: 'array', items: { type: 'string' } },
  },
}
const RESOLUTION_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['properties', 'ners', 'loops', 'findings', 'verdict'],
  properties: {
    properties: { type: 'object', additionalProperties: false, required: ['P_i', 'P_ii', 'P_iii', 'P_iv', 'P_v'], properties: { P_i: CRIT, P_ii: CRIT, P_iii: CRIT, P_iv: CRIT, P_v: CRIT } },
    ners: NERS_BLOCK,
    loops: { type: 'array', items: { type: 'object', additionalProperties: false, required: ['name', 'damper', 'cap', 'verdict'], properties: { name: { type: 'string' }, damper: { type: 'string' }, cap: { type: 'string' }, verdict: { type: 'string' } } } },
    findings: { type: 'array', items: FINDING },
    verdict: { type: 'string' },
  },
}
const RECONCILE_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['corpus', 'already_in_engine', 'improvements', 'reject', 'creative_layer', 'verdict'],
  properties: {
    corpus: { type: 'string' },
    already_in_engine: { type: 'array', items: { type: 'string' } },
    improvements: { type: 'array', items: { type: 'object', additionalProperties: false, required: ['id', 'what', 'mechanism', 'ners_impact', 'severity', 'adversarial_note'], properties: { id: { type: 'string' }, what: { type: 'string' }, mechanism: { type: 'string' }, ners_impact: { type: 'string' }, severity: { type: 'string', enum: ['high', 'medium', 'low'] }, adversarial_note: { type: 'string' } } } },
    reject: { type: 'array', items: { type: 'string' } },
    creative_layer: { type: 'array', items: { type: 'string' } },
    verdict: { type: 'string' },
  },
}
const VERIFY_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['target_id', 'real', 'ners_compliant', 'severity_adjust', 'reasoning', 'revised'],
  properties: {
    target_id: { type: 'string' },
    real: { type: 'boolean' },
    ners_compliant: { type: 'boolean' },
    severity_adjust: { type: 'string' },
    reasoning: { type: 'string' },
    revised: { type: 'string' },
  },
}
const DISTILL_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['cut', 'consolidate', 'keep_core', 'add_only_if', 'sequencing', 'headline'],
  properties: {
    cut: { type: 'array', items: { type: 'string' } },
    consolidate: { type: 'array', items: { type: 'string' } },
    keep_core: { type: 'array', items: { type: 'string' } },
    add_only_if: { type: 'array', items: { type: 'string' } },
    sequencing: { type: 'array', items: { type: 'string' } },
    headline: { type: 'string' },
  },
}

const CLUSTERS = [
  { key: 'measure_reach', title: 'Measure & reach', focus: `reach_base & reach_sigma (combat_systems.py:11,167), HEAD_REACH/LONG/HANDS2/reach_adj, REACH_W armour-rotation, the standing reach-disadvantage term in net_sigma. Reach is the dominant weapon driver (r=+0.83). Check: reach over-weighted vs delivery? point +1.0 reach makes thrusting rapier out-reach a greatsword? paired_short +1.4 reach_adj defensible? FOOT_MEASURE_K double-counting balance?` },
  { key: 'tempo_approach', title: 'Tempo, approach & stop-hit', focus: `weapon_tempo/close_tempo (combat_systems.py:17,32), approach_displace (209), close_rate & stop-hit (wrapper.py:66-85), ACT_THRESHOLD/BURST_MAX, CLOSE_TEMPO_COMPRESS. Check: is tempo a real second axis or compressed away? stop-hit pool=resolution_pool(history) only — fair sub-resolver? burst ceiling churn-positive?` },
  { key: 'reopen_recovery', title: 'Reopen / measure-recovery', focus: `reopen_moment creation a/b/c (wrapper.py:217-225), reopen_prob (combat_systems.py:217), push_avail. Check: are all three creation paths reachable & churn-positive? is longer-weapon reopen dominant or dead? does a spear actually re-make distance, or is it inert?` },
  { key: 'commit_disposition', title: 'Commit-depth & disposition', focus: `commit draw + disposition skew (wrapper.py:98-106), disp_lean (combat_systems.py:62), act_cost (47), OOB, three DISP hooks (config). Check: act_cost diverges from derived_stats §4.2 (state map F3)? disposition truly ~neutral (both poles cost)? is commit-depth a meaningful choice or RNG?` },
  { key: 'read_feint', title: 'Read, legibility & feint', focus: `reading (combat_systems.py:53), legibility (177), feint_eval (194), familiarity (tradition.py:62), mental_fat, read_win logistic (wrapper.py:133). Check: reading DOUBLE-weighted (Cog AND Att)? feint loop NERS-necessary or bolt-on? is precommit's ONLY consumption (def feint-resist) enough to justify the channel? legibility mode-shift correctness.` },
  { key: 'defence_modes', title: 'Defence modes (parry/dodge/wind)', focus: `mode_sigma (combat_systems.py:88), GATE table (74), guards, NEUTRALIZE_* fixed shapes, mode pick (wrapper.py:135-137). Check: is mode selection churn-positive or argmax-deterministic? GATE caps justified per weapon? does neutralize double-count defender skill (C-2 claims not — verify)?` },
  { key: 'initiative_vor', title: 'Initiative / Vor + Indes steal + counter', focus: `initiative_sigma/clamp/decay/hold (combat_systems.py:248-279), Vor loop (wrapper.py:41-46,148-154,229-230), Indes steal + INDES_SCALE, single-time counter (158,186-198), init_steal_factor/init_overcommit_loss. Check: Vor loop bounded (DECAY damper + CAP)? steal+counter a lever-pile or churn-rich? counter SUCCESS clamp [.05,.92]. ATTACKER_BIAS=0.12 vs mirror-fairness sound?` },
  { key: 'poststrike', title: 'Outcome map, overcommit, bind/kuzushi, riposte, displace', focus: `outcome mapping (wrapper.py:168-198), overcommit_exposure (163), bind loop + bind_sigma + KUZUSHI (combat_systems.py:228; wrapper.py:233-252), poise_factor (combat_systems.py:282), displace-and-step-inside (204-213), riposte/role-flip (253-261). Check: bind bounded (<=3 iters)? is poise churn-positive or a thin multiplier? is displace-inside reachable? overcommit→riposte loop check.` },
  { key: 'damage_armour', title: 'Damage chain & armour-defeat', focus: `core.py damage/coupling/p_auth/strike (34-99), RESIST/DELIVERY/QUAL/overwhelming tail, armor_defeat_sigma (combat_systems.py:110). Check: TWO percussion sources (p_auth vs hand-set w['percussion']) — drift? dead geo coefficients. linear (no-tanh) damage robust at extremes (no one-shot)? HEFT categorical {light:0,heavy:3} vs continuous MoI. ADEF_CUT=-0.9 a cliff?` },
  { key: 'tradition_layer', title: 'Tradition channel-weights & abilities', focus: `tradition.py whole file: TRADITIONS vectors, eff_cw wiring, ABILITIES (dead 'seize' → vorschlag/sen_no_sen inert; Japanese flagship can't fire), familiarity/ADJACENT, ability_armature.md drift. Check: do channel weights ROUTE the path or only tune σ? which traditions have ZERO live abilities (chinese/filipino)? is a native-tradition layer present at all? is 0.85/0.93/1.0 familiarity churn-positive?` },
  { key: 'wrapper_structure', title: 'Wrapper / loop / harness / portability', focus: `wrapper.py engagement() loop & terminals, fight() harness (275), role-object A/B architecture, mirror-fairness (tie coin-flip, alternating aggressor, ATTACKER_BIAS), beats<24, UPSET_FLOOR. Check PORTABILITY AS IT NOW STANDS, not as the pre-ED-1085 notes describe it: the sandbox imports are gone, so audit what replaced them — the sys.path.insert of __file__'s dir + _REPO_ROOT (core.py:13-17, wrapper.py:4, combat_systems.py:4) means this dir is scripts-on-path, NOT a package, and its modules import each other by bare name (import core, import weapon_physics). Is that survivable for the Godot port and for \`pytest tests/valoria\` collection? Does any module still assume an absolute path? fight()(sim) vs single-engagement(game) boundary clean? unreachable code (stamina<=-4 aborts)?` },
]

const CORPORA = [
  { key: 'weapon_physics', title: 'Weapon physics & balance', files: [`${DL}/weapon_physics_calibration_and_wiring_2026-06-22.md`, `${DL}/weapon_physics_preliminary_pob_2026-06-22.md`, `${DL}/weapon_tradition_state_analytical_ledger_2026-06-22.md`, `${DL}/weapon_physics_RECOVERED_composite_2026-06-22.py`, `${DL}/combat_analysis_rev2.md`], lens: `These derive reach/heft/tempo/str-demand/damage from physical primitives (mass, pob_frac, pommel_kg, MoI) and RETIRE categorical reach/wt. Some is ALREADY partly wired (p_auth). Claims: continuous MoI/heft replaces categorical {light,heavy}; new pommel_kg primitive; K_* gains UNCALIBRATED (need sim gate: mirror=50, attribute-tier spread, no-one-shot). Adversarial: is continuous heft NERS-Necessary or does categorical already deliver churn? Does wiring fix the two-percussion-source drift? Are the dead geo coefficients (thrust/cut/perc_conc) the natural consumers to wire? Is the analytical ledger's gap register (short-blunt class, dead levers, "traditions tune but never route") accurate vs HEAD or stale?` },
  { key: 'martial_morphology', title: 'Martial morphology (4 vols)', files: [`${DL}/martial_morphology_distilled.md`, `${DL}/martial_morphology_vol3_efficacy.md`, `${DL}/martial_morphology_vol2.md`, `${DL}/martial_morphology.md`], lens: `A morphology of martial traditions: 14 dimensions in 3 classes (efficacy-bearing / culture-framing / decisive variable = aliveness), the governing-analogue thesis, and a FOUR-AXIS evaluation standard (coherence / epistemic status / analogue-coherence / efficacy). tradition.py models traditions as cognitive-mode channel-vectors. Candidates: (a) four-axis standard as design discipline for the native-tradition layer; (b) skeleton-before-culture / efficacy-first order; (c) governing-analogue as the FLAVOUR layer — map to channel vectors? Be HARD-adversarial & judicious: vol3 says most of this is efficacy-NEUTRAL meaning, not mechanics. What is actually MECHANICALLY load-bearing for the resolver vs pure creative-layer? Does the aliveness axis even apply where every fighter is "alive"? Resist importing a 14-dim scheme the morphology's own distillation says should be cut to a few variables.` },
  { key: 'engagement_psych', title: 'Engagement psychology', files: [`${DL}/combat_engagement_engine_proposal.md`, `${DL}/combat_engagement_psychology_findings.md`], lens: `These self-audited down to ONE proposed mechanic: 'wariness' (commit-depth only, scaled by 1-familiarity), plus a regime-contest lens and a clinch/disengage-on-overcommit hook. They claim the engine ALREADY encodes disguise(legibility)/deception(feint)/overcommit-exploit faithfully — verify vs HEAD. Adversarial on the ONE addition: is 'wariness' NERS-Necessary or does disposition+familiarity already cover it? Is the regime-contest a real engine gap (no clinch/disengage contact axis — confirm) or out of scope? Is the §2 "convergence" circular (shared Silver + shared synthesizer)? Judge whether even the one mechanic earns its place.` },
  { key: 'deliberation', title: 'Deliberation-as-game', files: [`${DELIB}/deliberation-as-game-synthesis.md`], lens: `About DEBATE/TRIAL/NEGOTIATION as rule-governed games — NOT personal combat directly. Direct relevance likely to a parallel SOCIAL-contest engine (repo has one, git J-31). Be judicious: extract only what transfers. Candidates: (a) COMMITMENT STORE / game-state ledger (Hamblin) ↔ the engine's initiative/Vor ledger as a commitment record; (b) information-contest frame (sense more, reveal less) ↔ read/feint/legibility; (c) constitutive vs regulative rules, magic-circle/bounded-arena, adjudicator-as-resolver; (d) mixed-motive vs zero-sum (combat is zero-sum; deliberation often not) — implication for whether the SAME resolver serves both. Strongest honest output: does this argue for a SHARED resolver architecture across personal-combat + social-contest, and what would that share? Do NOT force combat-specific mechanics out of it.` },
]

// resume hardening: opus-tier stages (resolution/reconcile/adversarial/distill) errored on an opus
// availability blip in run 1. A() retries on null; RESUME_SALT changes their cache key so they re-run
// live on resume (the Sonnet module agents keep raw agent() → identical key → cache-hit, instant).
const RESUME_SALT = '\n\n[resume-pass:2 — re-run opus stage]'
async function A(p, o) {
  for (let i = 0; i < 3; i++) {
    const r = await agent(p + RESUME_SALT, o)
    if (r) return r
    log(`retry ${(o && o.label) || 'agent'} (attempt ${i + 1} returned null)`)
  }
  return await agent(p + RESUME_SALT, o)
}

phase('Module-NERS')
const round1 = await parallel([
  ...CLUSTERS.map(c => () => agent(
    `${SHARED}\n\n=== YOUR MODULE: ${c.title} (${c.key}) ===\nAudit ONLY this cluster. Read the cited files/functions in full first.\nFOCUS: ${c.focus}\n\nProduce: the IN->resolver->OUT contract (consumes, emits, dead-data, orphans); a per-criterion NERS verdict (N/R/S/E each pass/fail/partial with a one-line reason grounded in code); a churn assessment (does it branch the path / create meaningful choice, or only tune a number / sit inert?); a findings list (severity, kind, claim, file:line) — hunt for MORE than the verified facts; and concrete recommendations. Be adversarial: assume the module is broken and prove it or clear it.`,
    { schema: MODULE_SCHEMA, label: `module:${c.key}`, phase: 'Module-NERS', model: 'sonnet' }
  )),
  (() => A(
    `${SHARED}\n\n=== RESOLUTION DIAGNOSTIC (Instance A property test) ===\nRun valoria-resolution-diagnostic on the CORE RESOLVER and every embedded sub-resolver. READ FIRST: core.py (resolve/degree/roll_net/damage), and the substrate at ${SUBSTRATE}/ (m1_dice_sigma_core.py for soft_cap & sigma_n & the net distribution; r1_sigma_resolution.py for effective_ob & degree & resolution_pool; r8_parity_harness.py for WoundTracker). Then sub-resolvers in wrapper.py: read_win logistic (133), stop-hit roll (75-82), bind logistic loop (243-252), counter-success clamp (188-192), mode fallback (137), net_sigma assembly (140-144).\n\nTest P-i..P-v. Verify: (1) leverage σ_N-scaled uniform (soft_cap*sigma_n) — confirm by reading m1; (2) ER-2 continuity present in degree() and CORRECT; (3) wound-reduced pool regime — pool=max(1, resolution_pool(history)-wounds) can fall to ~1-2D (sub-5D) → does continuity cover it, or does a low-history wounded fighter hit a fidelity/cliff zone?; (4) μ-shift vs Ob-shift consequences for the degree ladder (overwhelming/failure rates); (5) Ob>=1 floor; (6) the embedded LOGISTIC sub-resolvers (read_win, bind, counter) — legible (P-i) or opaque secondary draws stacked on the main roll?; (7) loops: Vor (damper INIT_DECAY=.75, cap INIT_CAP=1.5), poise (recover+floor), burst (BURST_MAX) — each damped AND bounded?; (8) right engine for the pool regime (P-v)? Give a NERS verdict + loops table.`,
    { schema: RESOLUTION_SCHEMA, label: 'resolution-diagnostic', phase: 'Resolution', effort: 'high' }
  )),
  ...CORPORA.map(c => () => A(
    `${SHARED}\n\n=== CORPUS RECONCILIATION: ${c.title} ===\nRead these uploaded docs IN FULL:\n${c.files.map(f => '  - ' + f).join('\n')}\nThen read the relevant engine files to check what's ALREADY done vs proposed.\nLENS: ${c.lens}\n\nProduce: (a) already_in_engine — what the corpus proposes that HEAD already does (credit; flag where the corpus is STALE vs HEAD); (b) improvements — concrete NERS-assessed engine changes (what; mechanism as file/function/lever IN->OUT; ners_impact; severity; strongest case AGAINST); (c) reject — ideas NOT worth adopting + reason; (d) creative_layer — Jordan-only flavour; (e) verdict. Curious in extension, ADVERSARIAL in review (every addition risks lever-pile / NERS-N failure), judicious in reconciliation.`,
    { schema: RECONCILE_SCHEMA, label: `reconcile:${c.key}`, phase: 'Reconcile' }
  )),
])

const moduleResults = round1.slice(0, CLUSTERS.length).filter(Boolean)
const resolutionResult = round1[CLUSTERS.length] || null
const reconcileResults = round1.slice(CLUSTERS.length + 1).filter(Boolean)

// P7a · one module cluster returning nothing looks identical, in a total, to a clean module. Route
// each through the run so an empty cluster raises the alarm and a reader knows to check whether the
// agent read the file at all. Eleven clusters over one engine: silence from any of them is data.
for (const m of moduleResults) run.lens(`module:${m.module}`, m.findings || [])
if (resolutionResult) run.lens('resolution-diagnostic', resolutionResult.findings || [])
for (const r of reconcileResults) run.lens(`reconcile:${r.corpus}`, r.improvements || [])

const targets = []
for (const m of moduleResults) {
  for (const f of (m.findings || [])) {
    if (f.severity === 'P1' || f.severity === 'P2') targets.push({ id: `${m.module}:${f.id}`, kind: 'finding', payload: f, ctx: `module ${m.module}` })
  }
}
if (resolutionResult) for (const f of (resolutionResult.findings || [])) targets.push({ id: `resolution:${f.id}`, kind: 'finding', payload: f, ctx: 'resolution diagnostic' })
for (const r of reconcileResults) {
  for (const imp of (r.improvements || [])) {
    if (imp.severity === 'high' || imp.severity === 'medium') targets.push({ id: `${r.corpus}:${imp.id}`, kind: 'addition', payload: imp, ctx: `corpus ${r.corpus}` })
  }
}
targets.sort((a, b) => {
  const score = t => (t.kind === 'addition' ? 2 : 0) + (t.payload && t.payload.severity === 'P1' ? 1 : 0)
  return score(b) - score(a)
})
log(`Adversarial targets: ${targets.length} (${targets.filter(t => t.kind === 'addition').length} additions, ${targets.filter(t => t.kind === 'finding').length} findings)`)
const MAX_TARGETS = 40
const capped = targets.slice(0, MAX_TARGETS)
if (targets.length > MAX_TARGETS) log(`NOTE: capped adversarial verification at ${MAX_TARGETS}/${targets.length} targets (additions + P1s prioritized)`)
// The cap is a real coverage hole, not a footnote: everything past it returns UNREFUTED and would
// otherwise sit in the output looking exactly like a finding that survived a critic. §0.1 point 5's
// no-silent-caps rule — the run records it, and stop_reason carries it to the reader.
run.critiqued('Adversarial', targets.length, capped.length)

phase('Adversarial')
const verdicts = (await parallel(capped.map((t, i) => () => run.attempt('Adversarial', A(
  `${SHARED}\n\n=== ADVERSARIAL VERIFICATION (target ${i + 1}) ===\nFrom: ${t.ctx}. Target kind: ${t.kind}.\nTARGET (JSON): ${JSON.stringify(t.payload)}\n\nRun to BREAK it, not bless it. Read the cited code yourself.\n- FINDING: is the claim true against HEAD? severity right? could it be a deliberate, safeguarded design choice (intent gate)? stale (already fixed)?\n- ADDITION (corpus improvement): the bar is NERS-Necessary. Does the engine ALREADY deliver this churn another way? Would it be a lever-pile (E/N fail)? Does it preserve mirror-fairness & invariants? Gated on an UNRUN sim? Default to skepticism — most additions should be rejected or deferred unless they CONSOLIDATE or fix a real dead/broken path.\nReturn target_id="${t.id}", real, ners_compliant, a severity adjustment, adversarial reasoning (what survived the attack), and a revised recommendation.`,
  hCritic({ schema: VERIFY_SCHEMA, label: `verify:${t.id}`, phase: 'Adversarial' })
))))).filter(Boolean)

// P8 · a verdict of NOT-real, or an addition that fails NERS-Necessary, is the skeptic disagreeing
// with the producer. The Distill stage already had to reconcile these; it was doing so against an
// unstructured list, with nothing recording which disputes it silently dropped.
const byTarget = new Map(capped.map((t) => [t.id, t]))
for (const v of verdicts) {
  const t = byTarget.get(v.target_id)
  if (!t) continue
  const contested = (t.kind === 'finding' && v.real === false) || (t.kind === 'addition' && v.ners_compliant === false)
  if (!contested && !v.severity_adjust) continue
  run.dispute({
    finding_id: v.target_id,
    layer_disputed: contested ? (t.kind === 'addition' ? 'method' : 'evidence') : 'severity',
    root_cause: contested ? (t.kind === 'addition' ? 'scope-boundary' : 'measurement-vs-assertion') : 'severity-calibration',
    positions: [
      { by: t.ctx, holds: String((t.payload && (t.payload.claim || t.payload.what)) || '').slice(0, 400) },
      { by: 'skeptic', holds: String(v.reasoning || '').slice(0, 400), real: v.real, ners_compliant: v.ners_compliant },
    ],
    resolution_model: 'adjudicated-by-synthesis',
  })
}

// P7b · rank by independent rediscovery across the eleven module clusters + the resolution
// diagnostic. A defect three unrelated clusters hit while auditing different parts of the engine is
// a structural problem; one cluster hitting it hard may be one cluster's reading. The fan-out
// already produced this signal every run and discarded it at the return.
const allFindings = [].concat(
  ...moduleResults.map((m) => (m.findings || []).map((f) => Object.assign({ lens: `module:${m.module}` }, f))),
  ((resolutionResult && resolutionResult.findings) || []).map((f) => Object.assign({ lens: 'resolution' }, f)),
)
const ranked = hRediscover(allFindings, (f) => f.lens)
const corroborated = ranked.filter((g) => g.rediscovery > 1)
log(`Rediscovery: ${corroborated.length}/${ranked.length} distinct finding(s) surfaced independently by 2+ clusters`)

phase('Distill')
const compact = {
  modules: moduleResults.map(m => ({ module: m.module, ners: m.ners, churn: m.churn, findings: m.findings, recs: m.recommendations })),
  resolution: resolutionResult,
  reconcile: reconcileResults.map(r => ({ corpus: r.corpus, already: r.already_in_engine, improvements: r.improvements, reject: r.reject, creative: r.creative_layer, verdict: r.verdict })),
  verdicts,
  disagreements: run.disagreements,
  rediscovery: ranked.map(g => ({ key: g.key, rediscovery: g.rediscovery, lenses: g.lenses })),
}
const DISTILL_SCHEMA_ADJ = Object.assign({}, DISTILL_SCHEMA, {
  required: DISTILL_SCHEMA.required.concat(['adjudications']),
  properties: Object.assign({}, DISTILL_SCHEMA.properties, {
    adjudications: {
      type: 'array',
      description: 'one entry per disagreement — REQUIRED, and an unruled dispute is a run signal, not a silent drop',
      items: {
        type: 'object', additionalProperties: false,
        required: ['finding_id', 'ruling', 'reasoning'],
        properties: {
          finding_id: { type: 'string' },
          ruling: { type: 'string', enum: ['producer-holds', 'skeptic-holds', 'split', 'unresolved'] },
          reasoning: { type: 'string' },
        },
      },
    },
  }),
})
const distill = await A(
  `${SHARED}\n\n=== DISTILLATION SYNTHESIS ===\nYou have all module audits, the resolution diagnostic, corpus reconciliations, and adversarial verdicts (JSON below). Produce a DISTILLATION PROPOSAL in the spirit of the martial-morphology "distilled core": cut the elaborate to the few load-bearing variables.\n\nGovern by NERS and the churn principle. Use the adversarial verdicts to DISCARD findings that did not survive and additions that failed NERS-N.\nProduce: cut (dead-data / inert levers / redundancy to remove — specific, file/lever); consolidate (two-into-one: percussion sources, categorical->continuous heft, redundant difficulty levers); keep_core (the minimal NERS-clean load-bearing core that MUST stay — what actually generates churn); add_only_if (corpus additions worth it ONLY under stated gates — e.g. weapon-physics wiring gated on mirror/tier/no-one-shot sim); sequencing (ordered plan: dead-data cull → consolidation → gated additions); and a one-paragraph headline.\n\nADJUDICATION IS REQUIRED, NOT OPTIONAL. \`disagreements\` below is every place a skeptic contradicted a producer. Return one \`adjudications\` entry per disagreement, ruling for one side with your own reading of the cited code. A dispute you cannot settle from the files is ruled "unresolved" WITH the specific check that would settle it — that is a real outcome. A dispute you simply do not mention is the failure this field exists to prevent: it disappears while looking resolved.\n\nWEIGHT BY CORROBORATION. \`rediscovery\` counts how many INDEPENDENT clusters surfaced each finding. Treat a defect three unrelated clusters hit as structural; treat a solitary one as one cluster's reading until you have checked it yourself.\n\nALL RESULTS (JSON):\n${JSON.stringify(compact)}`,
  { schema: DISTILL_SCHEMA_ADJ, label: 'distill', phase: 'Distill', effort: 'high' }
)
for (const a of ((distill && distill.adjudications) || [])) {
  run.adjudicate(a.finding_id, a.ruling + ': ' + a.reasoning, 'distill')
}

const summary = run.summary()
if (summary.degraded) log(`[harness] run degraded — stop_reason=${summary.stop_reason}; the results below are complete, read the signals before banking them`)

return {
  run: summary,
  modules: moduleResults,
  resolution: resolutionResult,
  reconcile: reconcileResults,
  adversarial: verdicts,
  rediscovery: ranked.map(g => ({ key: g.key, rediscovery: g.rediscovery, lenses: g.lenses })),
  corroborated,
  distillation: distill,
}
