export const meta = {
  name: 'wave0-preflight',
  description: 'W0b of the code-shape program (ED-IN-0091/ED-IN-0092): §5 Jordan docket as one decision surface + OI-55 detector integrity (re-scoped, verify-not-redo) + adversarial critic + bookkeeping',
  phases: [
    { title: 'Produce', detail: 'docket (opus) + two detector lanes (sonnet), file-disjoint so no worktree isolation needed', model: 'opus/sonnet' },
    { title: 'Critic', detail: 'read-only adversarial relay over the three outputs (agonist->antagonist, output only)', model: 'opus' },
    { title: 'Bookkeeping', detail: '04_execution_ledger.md + HANDOFF_IN + ED-IN-0092 ledger entry', model: 'sonnet (effort low)' },
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
// W0b executes Wave 0 stages 1/2/4 of audit/2026-07-29-code-shape-open-items/01_orchestration_plan_v1.md
// (stage 3, the ED pre-allocation, shipped separately as the W0a micro-PR — Jordan's split, PR #256).
// Write lanes are FILE-DISJOINT (docket file vs structure_audit.py+its tests vs vector_audit tests),
// so no worktree isolation is needed (§4 requires it only for colliding write lanes).
// G12 preflight facts the orchestrator verified in-tree, binding on the agents below:
//   - The register's OI-55 `__init__`-misresolution half is ALREADY FIXED (commit f4ab261,
//     ED-MB-0043) with 4 regression tests at tests/valoria/test_structure_audit.py:157-213.
//     Verify, do not re-implement.
//   - tests/valoria/test_vector_audit.py already has ~19 tests; the register's "one total-pin"
//     claim is stale. Audit for genuine gaps only.
//   - review_core has no stubs.count signal yet (that is Wave 1's job, not W0b's).
// ---------------------------------------------------------------------------------------------

const run = hRun('wave0-preflight')

const DOCKET_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['file', 'forks_authored', 'j_rows_mapped', 'tiering', 'defaults_missing', 'notes'],
  properties: {
    file: { type: 'string' },
    forks_authored: { type: 'integer' },
    j_rows_mapped: { type: 'integer' },
    tiering: { type: 'array', items: { type: 'string' } },
    defaults_missing: { type: 'array', items: { type: 'string' } },
    notes: { type: 'string' },
  },
}

const DETECTOR_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['files_touched', 'tests_added', 'already_done_verified', 'delta', 'falsifier', 'notes'],
  properties: {
    files_touched: { type: 'array', items: { type: 'string' } },
    tests_added: { type: 'array', items: { type: 'string' } },
    already_done_verified: { type: 'array', items: { type: 'string' } },
    delta: { type: 'string' },
    falsifier: { type: 'string' },
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

const BOOK_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['files_touched', 'ed_filed', 'notes'],
  properties: {
    files_touched: { type: 'array', items: { type: 'string' } },
    ed_filed: { type: 'string' },
    notes: { type: 'string' },
  },
}

phase('Produce')

const DOCKET_PROMPT = `You are the docket assembler for Wave 0 of the code-shape program (ED-IN-0091).
AUTHOR the file audit/2026-07-29-code-shape-open-items/05_jordan_docket_v1.md — the §5 "Held for
Jordan" table of audit/2026-07-29-code-shape-open-items/01_orchestration_plan_v1.md expanded into ONE
self-contained decision surface Jordan can rule on top-to-bottom without chasing pointers.

Sources, all in the working tree (read them, do not re-fetch anything):
- 01_orchestration_plan_v1.md §5 (the 14-fork table + J-completeness note + re-entry protocol for row 1).
- 00_open_items_register.md (the OI rows each fork cites — quote the load-bearing evidence).
- 02_disposition_map.md (the authoritative row->owner lines; your docket must agree with it).
- workplans/valoria_master_workplan_v6.md §5 (~line 296): the RULED row format — "fork · default ·
  blocks · home pointer, NO status column (resolution lives in the ledger/handoffs)", tiered
  T0 / T1 / T2 sections. Adopt that format; keep the plan's # and OI columns as additions.
- For each fork's OPTIONS: chase its underlying sources and state the concrete options inline —
  e.g. fork 3 = ED-1051 (engine_clock doc:null flip; the long-standing default), fork 6 =
  ED-SC-0004 (legacy stub vs sigma-kernel, registers/editorial_ledger_sc.jsonl), fork 10 =
  ED-IN-0029 docket (UNRULED — reproduce its option labels, do not re-derive), fork 12 =
  registers/placeholder_names.yaml rows, fork 14 = ED-SC-0003..0005. Where the plan says
  "none named anywhere" (e.g. fork 4 env.crisis), present the option space honestly (consumer
  candidates from the contracts, or "ruled terminal") and mark NO DEFAULT loudly.

Hard requirements:
1. Status line: "## Status: DOCKET — HELD FOR JORDAN (ED-1094 exception: NOTHING here ratifies on
   merge) — ED-IN-0092, 2026-07-29" + a loud banner paragraph saying the same.
2. Tier every fork T0/T1/T2 with a one-line justification from its Blocks column (fork 3 is T0 —
   it is the sole remaining T0 blocker on M1).
3. J-completeness appendix: enumerate the register's 20 J-carrying rows (6 wholly J, 12 mixed, 2 D/J
   per the register's Counts section) and map each to a docket row or to the MB-fork visibility rows
   (OI-11 -> row 1, OI-21 -> row 2). Report the mapped count in your summary — if it is not 20,
   say which are missing rather than papering over.
4. Every numeric claim carries its source citation; invent nothing (no new constants, no invented
   defaults — a fork with no default stays "none").
5. Keep the file under ~12k tokens; terse rows, expansion only where a ruling genuinely needs context.

Return (summary only, not the file body): file path, forks_authored, j_rows_mapped, tiering (one
"row-N: T0/T1/T2" string per row), defaults_missing (rows offering no default), notes.`

const CLI_PROMPT = `Detector-integrity lane A of Wave 0 (OI-55 re-scoped; ED-IN-0092). Work in the
repo working tree. Read CLAUDE.md §0.1 first — every claim needs its artifact.

1. VERIFY, DO NOT REDO: the register's "__init__ relative-import misresolution" half of OI-55 is
   already fixed in skills/valoria-vector-audit/scripts/structure_audit.py (~lines 271-277, commit
   f4ab261) with 4 regression tests at tests/valoria/test_structure_audit.py:157-213. Run those
   tests, confirm green, and list them in already_done_verified. Change NOTHING about that fix.
2. IMPLEMENT the genuinely open half — CLI entry-point labeling. code_orphans (structure_audit.py
   ~lines 485-488) excludes only .__main__ suffixes and _private names, so any working CLI tool
   with zero importers reads as an orphan. Add entry-point detection at AST-collection time (a
   module containing an if __name__ == '__main__': guard) and surface a NEW labeled list
   cli_entries in the audit output, excluded from code_orphans. Single owner: the detection lives
   once in structure_audit.py; visible, never silent — both lists appear in the report/JSON.
3. TESTS (extend tests/valoria/test_structure_audit.py, known-answer fixtures over a synthetic
   tree): (a) a fake orphan MUST be reported; (b) a fake import cycle MUST be reported; (c) a
   module with a __main__ guard and zero importers MUST appear in cli_entries and MUST NOT appear
   in code_orphans; (d) a module with a __main__ guard that IS imported by another module must NOT
   be in cli_entries' orphan-exclusion path incorrectly (it is imported, so it was never an orphan
   candidate — assert it appears in neither list). Conditional assertions assert they asserted.
4. EXPECTED DELTA (§0.1): run the audit against the real tree BEFORE and AFTER your change; report
   "orphans N_before -> N_after, cli_entries M" in delta. Do not celebrate the shrink — record it.
Return: files_touched, tests_added, already_done_verified, delta, falsifier (the test name that
would catch a regression), notes.`

const VEC_PROMPT = `Detector-integrity lane B of Wave 0 (OI-55 re-scoped; ED-IN-0092). Work in the
repo working tree. Read CLAUDE.md §0.1 first.

The register claims skills/valoria-vector-audit/scripts/vector_audit.py's "analytical core has no
known-answer coverage beyond one total-pin". That claim is STALE — tests/valoria/test_vector_audit.py
has ~19 tests (banner_classify, diagnostics, build_g_key vs independent rederivation, Mode-D cascade
determinism, emit_structural_findings invariants, ...). Your job:
1. AUDIT: enumerate vector_audit.py's pure analytical functions and map each to its existing test
   (function name + test name) or mark it a genuine gap. Verify candidate gaps actually exist as
   named functions before testing them (the orchestrator's candidates: _median, _percentile_10_cut,
   validate, vocabulary_debt — treat as leads, not facts).
2. FILL: add known-answer tests ONLY for the genuine gaps, in tests/valoria/test_vector_audit.py —
   hand-computed inputs with hand-computed expected outputs (no snapshot-of-current-behavior tests:
   a known-answer test must be able to catch the function being wrong, not pin it being whatever it
   is). Touch NOTHING in vector_audit.py itself — tests only. If a gap function is unreachable dead
   code, record it in notes instead of testing it.
3. Report the covered-already map in already_done_verified (that is the G12 correction record for
   the stale register claim).
Return: files_touched, tests_added, already_done_verified (the function->test map), delta
("gaps found G, filled F"), falsifier (the test that would catch a wrong implementation), notes.`

const [docket, cliLane, vecLane] = await parallel([
  () => agent(DOCKET_PROMPT, { schema: DOCKET_SCHEMA, label: 'docket', phase: 'Produce', model: 'opus', effort: 'high' }),
  () => agent(CLI_PROMPT, { schema: DETECTOR_SCHEMA, label: 'detector:cli-entries', phase: 'Produce', model: 'sonnet', effort: 'high' }),
  () => agent(VEC_PROMPT, { schema: DETECTOR_SCHEMA, label: 'detector:vector-gaps', phase: 'Produce', model: 'sonnet', effort: 'high' }),
])

run.lens('docket', docket ? [docket] : [])
run.lens('detector:cli-entries', cliLane ? [cliLane] : [])
run.lens('detector:vector-gaps', vecLane ? [vecLane] : [])

phase('Critic')

const CRITIC_PROMPT = `Adversarial critic relay for Wave 0b of the code-shape program. You receive
the three producers' OUTPUT summaries below (never their reasoning) and the working tree. Try to
BREAK each one:
1. Docket (audit/2026-07-29-code-shape-open-items/05_jordan_docket_v1.md): independently recount
   the J-completeness mapping against 00_open_items_register.md's Counts section and
   02_disposition_map.md — is every one of the 20 J-carrying rows present or explicitly routed to
   an MB fork? Spot-check at least 4 forks' "default on offer" against their underlying sources
   (ED-1051, ED-SC-0004, ED-IN-0029, placeholder_names.yaml) — is any default invented rather than
   sourced? Is the ED-1094 held-back banner loud and unambiguous?
2. Detector lane A: does the cli_entries exclusion hide anything a triage SHOULD see? Read the diff
   to skills/valoria-vector-audit/scripts/structure_audit.py; for every module that moved out of
   code_orphans, check it really is a CLI entry (has a __main__ guard) and not a genuine dead
   module that happens to carry one. Are the four known-answer assertions real (would each fail on
   a planted regression)?
3. Detector lane B: are the new vector_audit tests known-answer (hand-computed expectations) or
   disguised snapshots of current behavior? Any claimed "already covered" mapping that is wrong?
Finding nothing is a real verdict — do not manufacture findings.

PRODUCER OUTPUT:
DOCKET: ${JSON.stringify(docket)}
LANE A: ${JSON.stringify(cliLane)}
LANE B: ${JSON.stringify(vecLane)}`

// run.attempt takes a PROMISE, not a thunk (harness line ~180). The first W0b run passed a thunk
// here, so the critic agent never spawned and the run degraded to null_result; caught by the
// harness's own null-result alarm, remediated by a standalone valoria-critic pass (same prompt,
// same producer outputs) gated by the orchestrator before commit. Fixed for future runs:
const critic = await run.attempt('critic:w0b',
  agent(CRITIC_PROMPT, hCritic({ schema: CRITIC_SCHEMA, label: 'critic:w0b', phase: 'Critic', model: 'opus', effort: 'high' })))

// ARITY, not just the method name. The owner's signature is
// `run.critiqued(stage, produced, reviewed)`; this call passed a single ARRAY, so
// `produced` was undefined, `undefined > 0` was false, and the critic-starvation signal
// could never fire from here. Same copy-paste lineage as the dispute defect eight lines
// below, and it survived that fix because the gate checked names and not shapes.
const CRITIQUED_STAGES = ['docket', 'detector:cli-entries', 'detector:vector-gaps']
run.critiqued('Critic', CRITIQUED_STAGES.length,
  (critic && critic.verdicts) ? CRITIQUED_STAGES.length : 0)
run.lens('critic:w0b', critic && critic.verdicts ? critic.verdicts : [])

const overturns = (critic && critic.verdicts ? critic.verdicts : []).filter(v => v.verdict !== 'uphold')
for (const v of overturns) {
  // Built by the owner, not by hand: the four keys this call used to pass ({layer,target,
  // detail,severity}) are none of them keys run.dispute() reads, so every dispute this
  // script ever recorded was keyed '?' and could not be adjudicated. See hVerdictDispute.
  run.dispute(hVerdictDispute(v, 'critic:w0b', v.target))
}
// Disputes are adjudicated by the ORCHESTRATOR after the run (agonist->antagonist relay: the
// reconciliation binds in the orchestrator's window, not inside this script) — recorded here so
// the summary carries them; the run continues per the report-only ruling.

const ranked = hRediscover(
  [
    ...(critic && critic.verdicts ? critic.verdicts.map(v => ({ desc: v.target + ': ' + v.evidence, lens: 'critic' })) : []),
    ...(critic && critic.missing ? critic.missing.map(m => ({ desc: m, lens: 'critic-missing' })) : []),
  ],
  f => f.lens,
)

phase('Bookkeeping')

const BOOK_PROMPT = `Bookkeeping lane for Wave 0b (ED-IN-0092), AFTER the critic pass. Edit ONLY the
four surfaces named below — never any other lane's handoff (critic F12), never
references/id_reservations.yaml (frozen), never registers/review_baseline.yaml.

1. CREATE audit/2026-07-29-code-shape-open-items/04_execution_ledger.md — the program's single
   STATUS surface (01_orchestration_plan_v1.md §6; created here at W0 so every wave can append,
   with W5 completing the diff against 02_disposition_map.md — this timing resolves the plan's
   created-by-W5/appended-by-every-wave tension and is flagged in the W0b PR body). Header: role,
   the immutable-snapshot rule (register/plan/map never change; status lives HERE only), column
   format "OI/item · wave · PR · ED · falsifier artifact · outcome". Rows for W0a (PR #256, the
   7-lane pre-allocation + file freeze, no ED filed — reservation only) and W0b (this work:
   docket + OI-55 re-scoped detector fixes; note the two G12 corrections — the __init__ half and
   the one-total-pin claim were already fixed/stale, verified not redone).
2. APPEND the ED-IN-0092 entry to registers/editorial_ledger_in.jsonl — copy the field schema of
   the most recent entries in that file exactly; content: W0 preflight execution (docket authored
   as HELD FOR JORDAN, detector integrity re-scoped + landed, execution ledger created); cite
   ED-IN-0091 as parent and OI-55; needs_jordan true (the docket awaits rulings), status open until
   the forks are ruled.
3. UPDATE registers/handoffs/HANDOFF_IN.md's ED-IN-0091 [OPEN] entry: W0a merged as PR #256
   (id_reservations frozen, blocks reserved), W0b landed (docket at 05_jordan_docket_v1.md held
   for Jordan; detector fixes + deltas), next action = Wave 1 (stubwire + reach oracle + dispatch
   closure) after W0b merges.
4. ROOT HANDOFF.md: add ONE line to Next actions: the code-shape run is live, id_reservations.yaml
   frozen until W5, MB/PC sessions launchable from their reserved blocks, §5 docket awaiting
   Jordan at 05_jordan_docket_v1.md.
Return: files_touched, ed_filed (the ED id), notes.`

const book = await agent(BOOK_PROMPT, { schema: BOOK_SCHEMA, label: 'bookkeeping', phase: 'Bookkeeping', model: 'sonnet', effort: 'low' })
run.lens('bookkeeping', book ? [book] : [])

return {
  run: run.summary(),
  docket, cliLane, vecLane, critic, ranked, book,
  orchestrator_note: 'Disputes (if any) adjudicated by the orchestrator before commit; commit blocked until reconciled.',
}
