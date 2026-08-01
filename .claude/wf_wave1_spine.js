export const meta = {
  name: 'wave1-spine',
  description: 'W1 of the code-shape program (ED-IN-0091/ED-IN-0093): stubwire primitive + pipeline-reach oracle + dispatch closure (flag-OFF combat bridge) + OI-17 stub conversion + adjudication + critic',
  phases: [
    { title: 'Spine', detail: 'stubwire primitive + telemetry + audit attribute + stubs.count signal (the single new primitive of P1)', model: 'sonnet' },
    { title: 'Build', detail: 'reach oracle · dispatch closure (bridge flag-OFF, seam-respecting) · 2 stub-conversion lanes — file-disjoint', model: 'sonnet' },
    { title: 'Adjudicate', detail: 'Key IN -> resolver -> OUT contract closure of the combat bridge', model: 'opus' },
    { title: 'Critic', detail: 'read-only adversarial relay over the whole wave diff', model: 'opus' },
    { title: 'Bookkeeping', detail: 'execution ledger + HANDOFF_IN + ED-IN-0093 + baseline seed arithmetic', model: 'sonnet (effort low)' },
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
// W1 executes 01_orchestration_plan_v1.md §2 (the three P1 primitives) + §3 Wave 1. Binding terms:
// - SEAM (critic F2): combat_engine_v1/wrapper.py and every file under systems/combat/ are
//   PC-session-owned and byte-untouched here. The bridge consumes the wrapper's public API as-is;
//   any wrapper-side need STOPS the lane and files the item. faction_action.py:349 likewise.
// - GOLDENS: the bridge ships behind DISPATCH_COMBAT_BRIDGE, default OFF, and with the flag OFF
//   every existing golden must be BYTE-IDENTICAL (orchestrator runs the parity probe; a moved
//   golden in the OFF state stops the wave). The ON flip is a separately scheduled IN action
//   after PC E0-E3 merge — NOT in this wave.
// - Stub conversions EXCLUDE systems/mass_battle/sim/altonian_reinforcements.py (MB §12 I1) and
//   resolver.py:51 (benign abstract base, recorded not converted).
// - The stubwire API is PINNED here so parallel builders code against it while Spine implements:
//     engine/substrate/stubwire.py
//       @dataclass(frozen=True) class StubResult: stub: bool = True; module: str; io_contract: str; reason: str
//       def stub_resolve(module: str, io_contract: str, *, reason: str) -> StubResult
//       invocations: dict[str, int]  (module -> count, module-level, reset_invocations() for tests)
//   No standalone stub registry file: the flag is DERIVED from "imports stubwire" (structure_audit
//   gains a stub_wired node attribute) — single-owner rule applied to the flag itself (§2.1).
// - File-disjointness of the Build lanes (no worktrees needed): oracle -> engine/tests/ (new file);
//   dispatch -> engine/cross_scale/{scene_dispatch.py, combat_bridge.py(new)} + systems/fieldwork/sim/;
//   conversion lane 1 -> systems/factions/sim/ + systems/overview/sim/; conversion lane 2 ->
//   systems/{world,characters,threadwork,social_contest}/sim/ + engine/{cross_scale/articulation.py,
//   autoload/npc_ai.py}. Spine -> engine/substrate/ + tools/review_core.py + registers/review_baseline.yaml
//   + skills/valoria-vector-audit/scripts/structure_audit.py + tests/valoria/.
// ---------------------------------------------------------------------------------------------

const run = hRun('wave1-spine')

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

const COMMON = `Repo /home/user/ttrpg. Read CLAUDE.md §0/§0.1 first, then
audit/2026-07-29-code-shape-open-items/01_orchestration_plan_v1.md §2 + §3 Wave 1 (your governing
spec) and 00_open_items_register.md for your OI rows. G12: every register/plan claim about the tree
is a LEAD — re-verify at the cited file:line before acting; if a claim is stale, record it in your
notes and adapt rather than executing it verbatim. No numeric constant without a PP/ED provenance
line. Stubs return typed no-ops via stubwire — never invented values. If your task would require
editing systems/combat/**, combat_engine_v1/wrapper.py, faction_action.py:349,
references/id_reservations.yaml, or moving any golden: STOP that item, list it in stopped_items
with the reason, and continue with the rest.`

phase('Spine')

const spine = await agent(`${COMMON}

You build the ONE new primitive of P1 (plan §2.1): engine/substrate/stubwire.py, exactly to the
API pinned in this script's header comment (frozen StubResult dataclass; stub_resolve(module,
io_contract, *, reason); module-level invocations counter with a reset helper for tests). Then:
1. TELEMETRY: find the season loop's existing F7 telemetry pattern (engine/mc_v18.py — how
   npcs_generated reaches SeasonReport / the F7 smoke oracle) and fold a stub_hits counter into
   campaign telemetry the same way, byte-preserving all existing fields and goldens (flag nothing,
   change no existing value — additive only; if adding the field would move an existing golden's
   byte content, add it in a way that does not (e.g. only when nonzero) and record the choice).
2. AUDIT ATTRIBUTE: skills/valoria-vector-audit/scripts/structure_audit.py gains a stub_wired
   node attribute derived from "module imports engine.substrate.stubwire" (reuse the existing AST
   import pass — do NOT add a second parser; compose with what is there). Surface the count in the
   JSON + register output alongside orphans/cli_entries.
3. SIGNAL: tools/review_core.py gains a report-only stubs.count CHECKS row (mirror the existing
   row shape exactly — id/tier/lane/argv/count_re; the argv can invoke structure_audit or a small
   --stub-count mode that prints the count). registers/review_baseline.yaml gains the stubs.count
   entry mirroring the existing entry shape. SEED IT AT 0 WITH A LOUD TODO COMMENT: the real seed
   (the full expected converted set INCLUDING the MB-owned altonian_reinforcements, critic F4) is
   set by this wave's Bookkeeping stage from the measured post-conversion count + 1 — you cannot
   know it yet. Note: registers/review_baseline.yaml is Jordan-CODEOWNED; this seeding is the
   pre-declared Wave-1 protocol from the plan (stop-conditions list) — cite that in the diff comment.
4. FALSIFIER: tests/valoria/test_stubwire.py — a fixture module converted to stubwire; assert the
   audit attribute sees it, the invocations counter counts it, and the review_core signal counts it.
   Document the mutation check in the test docstring: deleting the fixture's stubwire import must
   fail all three assertions (and structure the test so that is actually true).
Return per LANE_SCHEMA (golden_status: state plainly whether any existing test/golden changed).`,
  { schema: LANE_SCHEMA, label: 'spine:stubwire', phase: 'Spine', model: 'sonnet', effort: 'high' })

run.lens('spine:stubwire', spine ? [spine] : [])

phase('Build')

const ORACLE_PROMPT = `${COMMON}

You build the acceptance oracle (plan §2.3, OI-56): engine/tests/test_pipeline_reach.py. A seeded,
deterministic mc_v18 campaign asserting plan §1's acceptance list with explicit coverage counting
(assert checked >= N per §0.1 #2 — a direction that never came up is a FAIL, not a skip):
- every scene_type the slate can queue resolves canonically or records a stubwire flag (consume the
  stub_hits telemetry / stubwire.invocations per the pinned API);
- the 7 Key-delivery directions (directional_coverage_v1.md's roster) each fire or stub-flag;
- world chains (world.npcs / world.knots / world.settlements) populated — xfail until Wave 2;
- zero unconditional NotImplementedError in live trees EXCEPT the single accepted cross-session
  handoff: systems/mass_battle/sim/altonian_reinforcements.py, which gets a NAMED xfail-manifest
  row citing "MB plan §12 I1" (critic F9).
Ship RED-marked: an explicit XFAIL_MANIFEST structure at module top, one row per unwired direction,
each citing its OI row (from 00_open_items_register.md) — the manifest IS the live P1 burn-down
list. Combat rows assert under the DISPATCH_COMBAT_BRIDGE flag and xfail while it is off (F2).
Strict rows this wave: the stub-flag paths your fellow lanes wire (dispatch stubwire fallback,
converted stub invocations). Use the smallest seeded campaign that exercises dispatch (mirror
test_f7_smoke_oracle.py's setup — read it first; do NOT re-record or alter it). Every xfail must
be an honest "not wired yet", never a disguised pass. Return per LANE_SCHEMA.`

const DISPATCH_PROMPT = `${COMMON}

You close dispatch (plan §2.2, OI-01 + OI-02) — one lane because both halves edit
engine/cross_scale/scene_dispatch.py:
1. Re-verify OI-01: the combat branch calls DEPRECATED systems.combat.sim.combat.resolve_combat_round
   (~:137-143) and defers on missing personal-combat actors. Then build
   engine/cross_scale/combat_bridge.py (NEW, IN-side of the seam): derives combat parties from the
   SAME faction aggregates the [SEED] pattern _emergency_council_parties established (find it —
   ED-SC-0006/0007, social-contest context derivation; cite it, reuse its derivation, invent no
   actors), calls combat_engine_v1/wrapper.py's PUBLIC resolve API as-is (read the wrapper to learn
   the API — you may NOT edit it or anything under systems/combat/), and returns the result into
   the dispatch slot. Gate the new path behind DISPATCH_COMBAT_BRIDGE, DEFAULT OFF, resolved the
   same way existing engine flags are (find the existing flag pattern — e.g. ECHO_TRANSPORT from
   ED-IN-0028 — and mirror it; single owner). With the flag OFF the branch behaves byte-identically
   to today (the deprecated call stays in place under OFF — retiring it happens at the ON flip, a
   separately scheduled action; make the OFF path provably unchanged).
2. CHARACTERIZATION TEST (shape/contract-level ONLY, critic F2 term 1): a new engine/tests test
   pinning the wrapper AT THE SEAM — result schema, determinism under a fixed seed, presence of
   exactly the fields the bridge consumes. NEVER a damage value, win rate, or balance quantity: a
   PC rebalance must not turn this test red. State that rule in the test docstring.
3. OI-02: convert systems/fieldwork/sim/fieldwork.py and investigation.py from raise-stubs to
   stubwire (pinned API; io_contract from their module contracts; reason cites the FI design gate).
   In scene_dispatch, DELETE the "resolver not live" silent-deferral string (~:214) — the fallback
   becomes a stubwire flag (visible), and the investigation/fieldwork scene_types route to the
   stub-wired resolvers. Every other scene_type in _resolve_slot: verify the mapping is total —
   canonical resolver or stubwire, no silent branch left; list the final mapping in your notes.
Return per LANE_SCHEMA (golden_status: MUST state the flag-OFF byte-identity claim and how you
verified it locally, e.g. targeted engine/tests run).`

const CONV1_PROMPT = `${COMMON}

Stub-conversion lane 1 (OI-17 slice; mechanical, uniform). Convert these raise-stub modules to the
pinned stubwire API — preserve each module's declared entry-point signatures, return a typed no-op
StubResult from stub_resolve('<dotted.module>', '<io summary from its module contract or docstring>',
reason='<the design gate, cited>'); keep any module docstring/provenance comments:
  systems/factions/sim/: charter_liberties, infrastructure_reclamation, home_sanctuary,
    varfell_mandate_action, varfell_territorial_acquisition, hafenmark_equipment
  systems/overview/sim/: rs_track, ip_track
FIRST re-verify each file is genuinely an unconditional-raise stub (G12); a file that has grown
real behavior since the register is SKIPPED with a note, not overwritten. EXCLUDED (do not touch):
altonian_reinforcements.py (MB-owned). Do not add tests per-module (test_stubwire covers the
pattern); do add each module to the reach oracle's expectations ONLY via your notes (the oracle
lane owns that file). Return per LANE_SCHEMA.`

const CONV2_PROMPT = `${COMMON}

Stub-conversion lane 2 (OI-17 remainder + OI-18a + OI-19 + OI-10a's stub-wire half). Same
conversion rules as lane 1 (pinned stubwire API, typed no-ops, G12 re-verify each site first):
  A. Full-module conversions: systems/world/sim/{miraculous_event, restoration_movement},
     systems/characters/sim/companion, systems/threadwork/sim/rendering,
     engine/cross_scale/articulation.py (self-flag ONLY — the minimal subscriber is Wave 2 item 6;
     the render layer stays ED-IN-0073's docket), engine/autoload/npc_ai.py.
  B. OI-18a (SELF-FLAG ONLY, plan Wave-1 scope note): the contest GAMES router's stub rows
     (systems/social_contest/sim/contest/wrapper.py GAMES dict ~:209-214 — verify, the docket
     corrected these line numbers; agon at :207 is WIRED, untouched) and the
     DyadicMode/NegotiationMode/CeremonialMode.play scaffolds (contest/modes.py ~:328-334): route
     their not-built paths through stubwire so invocation is visible. The actual game builds stay
     gated on the SC P0 docket (ED-SC-0003..0005, §5 fork 14) — build NOTHING.
  C. OI-19 partial branches: tribunal.py:149 (§7 Asymmetric Proceeding), treaty.py:107,
     contest/dictionaries.py:710 — convert the raising branch to a stubwire flag, leaving the
     live branches byte-identical. resolver.py:51 is a benign abstract base: verify and RECORD in
     notes, change nothing.
Return per LANE_SCHEMA.`

const [oracle, dispatch, conv1, conv2] = await parallel([
  () => agent(ORACLE_PROMPT, { schema: LANE_SCHEMA, label: 'build:reach-oracle', phase: 'Build', model: 'sonnet', effort: 'high' }),
  () => agent(DISPATCH_PROMPT, { schema: LANE_SCHEMA, label: 'build:dispatch-closure', phase: 'Build', model: 'sonnet', effort: 'high' }),
  () => agent(CONV1_PROMPT, { schema: LANE_SCHEMA, label: 'convert:factions-overview', phase: 'Build', model: 'sonnet', effort: 'low' }),
  () => agent(CONV2_PROMPT, { schema: LANE_SCHEMA, label: 'convert:world-contest-partials', phase: 'Build', model: 'sonnet', effort: 'low' }),
])

run.lens('build:reach-oracle', oracle ? [oracle] : [])
run.lens('build:dispatch-closure', dispatch ? [dispatch] : [])
run.lens('convert:factions-overview', conv1 ? [conv1] : [])
run.lens('convert:world-contest-partials', conv2 ? [conv2] : [])

phase('Adjudicate')

const adj = await agent(`${COMMON}

Contract-conformance adjudication of the combat bridge (module-adjudicator method: Key IN ->
resolver -> OUT closure). Read the dispatch lane's produced files (engine/cross_scale/combat_bridge.py,
the scene_dispatch diff, the characterization test) against references/module_contracts.yaml's
personal_combat rows and the wrapper's actual public surface. Adjudicate: (1) does the bridge
consume ONLY declared/public wrapper surface (no reach-ins past the seam)? (2) is the party
derivation faithful to the _emergency_council_parties [SEED] precedent (no invented actors, no
fabricated stats)? (3) is the characterization test genuinely shape-level (would a roster-wide
damage rebalance keep it green)? (4) with the flag OFF, is the old path provably untouched?
(5) are the emitted/returned Keys (if any) registered types? Produce closure_findings (one line
per defect or residual, file:line) and a verdict. You are read-only on intent — if a fix is
needed, name it; do not make it.
DISPATCH LANE OUTPUT: ${JSON.stringify(dispatch)}`,
  { schema: ADJ_SCHEMA, label: 'adjudicate:bridge', phase: 'Adjudicate', model: 'opus', effort: 'high' })

run.lens('adjudicate:bridge', adj && adj.closure_findings ? adj.closure_findings : [])

phase('Critic')

const critic = await run.attempt('critic:w1',
  agent(`Adversarial critic relay for Wave 1 of the code-shape program (repo /home/user/ttrpg).
You receive the producers' OUTPUT summaries (never their reasoning) and the working tree (git diff
shows the wave's changes). Try to BREAK the wave against its own exit criteria
(01_orchestration_plan_v1.md §3 Wave 1 Exit + §2):
1. SEAM: grep the diff for ANY touch of systems/combat/**, wrapper.py, faction_action.py — a
   single byte is a stop-condition violation.
2. FLAG-OFF PARITY: is DISPATCH_COMBAT_BRIDGE genuinely default-OFF, and is the OFF path
   byte-equivalent to the pre-wave behavior? Look for sneaky refactors of the old branch.
3. STUB CONVERSIONS: for each converted module, was it genuinely an unconditional-raise stub
   (check git log/diff), does it return a typed no-op (never a fabricated value), and does the
   set of converted files match the plan's OI-17/18a/19/10a scope EXACTLY — nothing extra
   (esp. altonian_reinforcements untouched, resolver.py:51 untouched), nothing dropped?
4. ORACLE HONESTY: is every xfail row an honest not-wired citation (OI row named), or does any
   xfail mask a should-be-strict assertion? Does any "strict" row actually assert (assert
   checked >= N present)? Is the altonian manifest row present and citing MB §12 I1?
5. CHARACTERIZATION TEST: does it pin any outcome/balance value (it must not)?
6. TELEMETRY: did stub_hits change any existing golden's bytes?
Verdicts per target with severity + file:line evidence; finding nothing is a real verdict.
PRODUCER OUTPUT:
SPINE: ${JSON.stringify(spine)}
ORACLE: ${JSON.stringify(oracle)}
DISPATCH: ${JSON.stringify(dispatch)}
CONV1: ${JSON.stringify(conv1)}
CONV2: ${JSON.stringify(conv2)}
ADJUDICATOR: ${JSON.stringify(adj)}`,
    hCritic({ schema: CRITIC_SCHEMA, label: 'critic:w1', phase: 'Critic', model: 'opus', effort: 'high' })))

run.critiqued(['spine:stubwire', 'build:reach-oracle', 'build:dispatch-closure', 'convert:factions-overview', 'convert:world-contest-partials'])
run.lens('critic:w1', critic && critic.verdicts ? critic.verdicts : [])

const overturns = (critic && critic.verdicts ? critic.verdicts : []).filter(v => v.verdict !== 'uphold')
for (const v of overturns) {
  // Built by the owner, not by hand: the four keys this call used to pass ({layer,target,
  // detail,severity}) are none of them keys run.dispute() reads, so every dispute this
  // script ever recorded was keyed '?' and could not be adjudicated. See hVerdictDispute.
  run.dispute(hVerdictDispute(v, 'critic:w1', v.target))
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

Bookkeeping for Wave 1 (ED-IN-0093), AFTER the critic. Edit ONLY: the execution ledger, the IN
handoff, root HANDOFF.md, registers/editorial_ledger_in.jsonl, and the ONE pre-declared baseline
seed. Never any other lane's handoff; never id_reservations.yaml.
1. BASELINE SEED (the pre-declared Wave-1 protocol): measure the post-conversion stub_wired count
   (run the structure_audit or the review_core stubs.count signal), add 1 for the MB-owned
   altonian_reinforcements.py (critic F4 — seed at the FULL expected set so MB's later conversion
   moves the count toward, never past, the ceiling), and set registers/review_baseline.yaml's
   stubs.count baseline to that number, replacing the Spine stage's seeded 0 + TODO. Show the
   arithmetic in the YAML comment (measured N + 1 = seed).
2. audit/2026-07-29-code-shape-open-items/04_execution_ledger.md: append rows (same column
   format) for OI-56 (oracle), OI-01 (bridge, FLAG-OFF, ON-flip deliberately not scheduled here),
   OI-02, OI-17 (converted list + the two exclusions), OI-18a, OI-19 (incl. resolver.py:51
   recorded-benign), OI-10a, and the stubs.count ratchet seeding.
3. registers/editorial_ledger_in.jsonl: append ED-IN-0093 (schema-copy the latest entries; parent
   ED-IN-0091; status open only if something genuinely awaits Jordan — otherwise resolved;
   describe the wave in 3-4 sentences incl. the flag-OFF term and the seed arithmetic).
4. registers/handoffs/HANDOFF_IN.md: update the ED-IN-0091 program entry — W1 landed (what),
   next = Wave 2 (orphan closure seams). Root HANDOFF.md: update the program's one line only if
   its content changed (the docket pointer etc. stays).
Validate the JSONL after editing (python3 -c "import json; [json.loads(l) for l in open(...)]").
Return per LANE_SCHEMA (falsifier: the baseline-seed arithmetic line).`,
  { schema: LANE_SCHEMA, label: 'bookkeeping', phase: 'Bookkeeping', model: 'sonnet', effort: 'low' })

run.lens('bookkeeping', book ? [book] : [])

return {
  run: run.summary(),
  spine, oracle, dispatch, conv1, conv2, adj, critic, ranked, book,
  orchestrator_note: 'Orchestrator gates before commit: byte-parity probe (flag OFF, full engine/tests + pytest vs pre-wave), critic dispute reconciliation, G12 re-derivation of the seed arithmetic and conversion census.',
}
